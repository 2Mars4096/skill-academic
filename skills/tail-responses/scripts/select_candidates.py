#!/usr/bin/env python3
"""Select a baseline and diverse outliers from an assessed semantic matrix."""

import argparse
import json
import math
import sys


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def select(data):
    if not isinstance(data, dict):
        raise ValueError("input must be an object")
    for key in ("comparison_method", "sampling_mode"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    rows = data.get("candidates")
    matrix = data.get("similarity")
    if not isinstance(rows, list) or not isinstance(matrix, list):
        raise ValueError("candidates and similarity must be arrays")
    n = len(rows)
    if len(matrix) != n or any(not isinstance(r, list) or len(r) != n for r in matrix):
        raise ValueError("similarity must be an N by N matrix")
    ids = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("each candidate must be an object")
        for key in ("id", "family"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f"candidate {key} must be a nonempty string")
        if row["id"] in ids:
            raise ValueError("candidate IDs must be unique")
        ids.add(row["id"])
        if type(row.get("eligible")) is not bool:
            raise ValueError("eligible must be boolean")
        for key in ("usefulness", "feasibility", "confidence"):
            if key not in row:
                raise ValueError(f"missing {key}")
            val = row[key]
            if val is None and key != "usefulness":
                continue
            if type(val) is not int or val not in (1, 2, 3):
                raise ValueError(f"invalid {key} rating")
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            if not number(value) or not 0 <= value <= 1:
                raise ValueError("similarities must be finite numbers in [0,1]")
        if abs(matrix[i][i] - 1) > 1e-8:
            raise ValueError("matrix diagonal must be 1")
    for i in range(n):
        for j in range(i):
            if abs(matrix[i][j] - matrix[j][i]) > 1e-8:
                raise ValueError("matrix must be symmetric")
    threshold = data.get("duplicate_threshold", 0.9)
    if not number(threshold) or not 0 < threshold <= 1:
        raise ValueError("duplicate_threshold must be in (0,1]")
    tail_only = data.get("tail_only", False)
    if type(tail_only) is not bool:
        raise ValueError("tail_only must be boolean")
    eligible = [i for i, row in enumerate(rows) if row["eligible"]]
    k = min(3, max(0, len(eligible) - 1))
    novelty = {}
    for i in eligible:
        distances = sorted(1 - matrix[i][j] for j in eligible if i != j)
        novelty[i] = sum(distances[:k]) / k if k else None

    def quality(i):
        return tuple(rows[i][key] or 0 for key in ("usefulness", "feasibility", "confidence"))

    selected = []
    roles = []
    if eligible and not tail_only:
        families = {}
        for i in eligible:
            families.setdefault(rows[i]["family"], []).append(i)
        family = max(families.values(), key=lambda members: (len(members), max(quality(i) for i in members)))
        baseline = max(family, key=lambda i: (
            sum(matrix[i][j] for j in family if j != i) / max(1, len(family) - 1),
            quality(i), -i))
        selected.append(baseline)
        roles.append("Baseline")
    while len(selected) < 4:
        remaining = [i for i in eligible if i not in selected
                     and all(matrix[i][j] < threshold for j in selected)]
        if not remaining:
            break
        represented = {rows[i]["family"] for i in selected}
        wild = len(selected) == 3

        def rank(i):
            local = novelty[i] if novelty[i] is not None else 0
            separation = min((1 - matrix[i][j] for j in selected), default=local)
            score = local if wild else (local + separation) / 2
            return (rows[i]["family"] not in represented, score, quality(i), -i)

        chosen = max(remaining, key=rank)
        selected.append(chosen)
        roles.append("Wild card" if wild else "Rare alternative")
    return {
        "comparison_method": data["comparison_method"],
        "sampling_mode": data["sampling_mode"],
        "pool_count": n,
        "eligible_count": len(eligible),
        "neighbors": k,
        "excluded_ids": [row["id"] for row in rows if not row["eligible"]],
        "selected": [dict(candidate=rows[i], role=role,
                          novelty=round(novelty[i], 6) if novelty[i] is not None else None)
                     for i, role in zip(selected, roles)],
        "shortfall": 4 - len(selected),
        "limitation": ("Fewer than four eligible, sufficiently distinct candidates; no padding."
                       if len(selected) < 4 else None),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON pool file, or - for stdin")
    args = parser.parse_args()
    try:
        if args.input == "-":
            data = json.load(sys.stdin)
        else:
            with open(args.input, encoding="utf-8") as source:
                data = json.load(source)
        result = select(data)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\n")
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False, allow_nan=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
