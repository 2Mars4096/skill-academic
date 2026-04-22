#!/usr/bin/env python3
"""Deterministically rank strategy candidates from a JSON or YAML ledger."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

TEXT_SCALE = {
    "none": 0.0,
    "unknown": 0.0,
    "low": 0.25,
    "medium": 0.5,
    "med": 0.5,
    "high": 0.75,
    "very-high": 1.0,
    "very_high": 1.0,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score strategies from a JSON or YAML strategy ledger.",
    )
    parser.add_argument("ledger", help="Path to a JSON, YAML, or YML ledger file")
    parser.add_argument("--top", type=int, default=0, help="Show only the top N entries")
    parser.add_argument(
        "--include-killed",
        action="store_true",
        help="Include killed strategies in the ranking output",
    )
    parser.add_argument(
        "--exploration-weight",
        type=float,
        default=0.35,
        help="Weight applied to exploration bonus",
    )
    parser.add_argument(
        "--cost-weight",
        type=float,
        default=0.25,
        help="Weight applied to the cost penalty",
    )
    parser.add_argument(
        "--risk-weight",
        type=float,
        default=0.20,
        help="Weight applied to the risk penalty",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the ranked output as JSON instead of a table",
    )
    return parser.parse_args()


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def parse_scalar(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        raw = value.strip().lower()
        if not raw:
            return default
        if raw.endswith("%"):
            try:
                return float(raw[:-1]) / 100.0
            except ValueError:
                return default
        if raw in TEXT_SCALE:
            return TEXT_SCALE[raw]
        try:
            return float(raw)
        except ValueError:
            return default
    return default


def load_ledger(path: Path) -> Any:
    suffix = path.suffix.lower()
    content = path.read_text()

    if suffix == ".json":
        return json.loads(content)

    if suffix in {".yaml", ".yml"}:
        try:
            import yaml
        except ImportError as exc:
            raise SystemExit(
                "YAML input requires PyYAML to be installed; use JSON instead."
            ) from exc
        return yaml.safe_load(content)

    raise SystemExit("Ledger must be .json, .yaml, or .yml")


def extract_strategies(ledger: Any) -> list[dict[str, Any]]:
    if isinstance(ledger, list):
        strategies = ledger
    elif isinstance(ledger, dict):
        strategies = ledger.get("strategies", [])
    else:
        raise SystemExit("Ledger must be a list or a dict with a 'strategies' key")

    if not isinstance(strategies, list):
        raise SystemExit("'strategies' must be a list")

    cleaned: list[dict[str, Any]] = []
    for item in strategies:
        if not isinstance(item, dict):
            raise SystemExit("Each strategy entry must be an object")
        cleaned.append(item)
    return cleaned


def average_reward(strategy: dict[str, Any]) -> float:
    direct = strategy.get("average_reward", strategy.get("reward"))
    if direct is not None:
        return clamp(parse_scalar(direct), -1.0, 1.0)

    rewards = strategy.get("rewards")
    if isinstance(rewards, list) and rewards:
        values = [parse_scalar(item) for item in rewards]
        return clamp(sum(values) / len(values), -1.0, 1.0)

    return 0.0


def confidence_score(strategy: dict[str, Any]) -> float:
    direct = strategy.get("confidence", strategy.get("evidence_strength"))
    if direct is not None:
        return clamp(parse_scalar(direct), 0.0, 1.0)

    evidence_count = parse_scalar(strategy.get("evidence_count"))
    return clamp(evidence_count / 4.0, 0.0, 1.0)


def choose_action(priority: float, reward: float, confidence: float, novelty: float) -> str:
    if reward >= 0.6 and confidence >= 0.6:
        return "exploit"
    if novelty >= 0.6 and confidence < 0.5:
        return "explore"
    if reward >= 0.25:
        return "mutate"
    if priority <= 0.0:
        return "kill"
    return "park"


def rank_strategies(
    strategies: list[dict[str, Any]],
    include_killed: bool,
    exploration_weight: float,
    cost_weight: float,
    risk_weight: float,
) -> list[dict[str, Any]]:
    ranked = []
    for strategy in strategies:
        status = str(strategy.get("status", "live")).strip().lower() or "live"
        if status == "killed" and not include_killed:
            continue

        reward = average_reward(strategy)
        confidence = confidence_score(strategy)
        novelty = clamp(parse_scalar(strategy.get("novelty"), 0.0), 0.0, 1.0)
        cost = clamp(
            parse_scalar(strategy.get("cost", strategy.get("execution_cost")), 0.0),
            0.0,
            1.0,
        )
        risk = clamp(parse_scalar(strategy.get("risk"), 0.0), 0.0, 1.0)
        evidence_count = int(round(parse_scalar(strategy.get("evidence_count"), 0.0)))

        exploration_bonus = exploration_weight * (1.0 - confidence) * novelty
        cost_penalty = cost_weight * cost
        risk_penalty = risk_weight * risk
        priority = reward + exploration_bonus - cost_penalty - risk_penalty

        ranked.append(
            {
                "id": strategy.get("id", "<missing-id>"),
                "status": status,
                "priority": round(priority, 4),
                "average_reward": round(reward, 4),
                "confidence": round(confidence, 4),
                "novelty": round(novelty, 4),
                "cost": round(cost, 4),
                "risk": round(risk, 4),
                "evidence_count": evidence_count,
                "next_action": strategy.get(
                    "next_action",
                    choose_action(priority, reward, confidence, novelty),
                ),
                "failure_reason": strategy.get("failure_reason", ""),
                "thesis": strategy.get("thesis", ""),
            }
        )

    ranked.sort(
        key=lambda item: (
            item["priority"],
            item["average_reward"],
            item["confidence"],
            item["novelty"],
        ),
        reverse=True,
    )
    return ranked


def print_table(ranked: list[dict[str, Any]], top: int) -> None:
    rows = ranked[:top] if top > 0 else ranked
    if not rows:
        print("No strategies to rank.")
        return

    header = (
        f"{'rank':<4} {'id':<28} {'status':<9} {'priority':>8} "
        f"{'reward':>7} {'conf':>6} {'novel':>6} {'cost':>6} {'risk':>6} {'action':<8}"
    )
    print(header)
    print("-" * len(header))
    for index, item in enumerate(rows, start=1):
        print(
            f"{index:<4} "
            f"{str(item['id'])[:28]:<28} "
            f"{item['status'][:9]:<9} "
            f"{item['priority']:>8.3f} "
            f"{item['average_reward']:>7.3f} "
            f"{item['confidence']:>6.2f} "
            f"{item['novelty']:>6.2f} "
            f"{item['cost']:>6.2f} "
            f"{item['risk']:>6.2f} "
            f"{str(item['next_action'])[:8]:<8}"
        )


def main() -> int:
    args = parse_args()
    ledger_path = Path(args.ledger).expanduser().resolve()
    if not ledger_path.exists():
        print(f"Ledger not found: {ledger_path}", file=sys.stderr)
        return 1

    ledger = load_ledger(ledger_path)
    strategies = extract_strategies(ledger)
    ranked = rank_strategies(
        strategies=strategies,
        include_killed=args.include_killed,
        exploration_weight=args.exploration_weight,
        cost_weight=args.cost_weight,
        risk_weight=args.risk_weight,
    )

    if args.json:
        rows = ranked[: args.top] if args.top > 0 else ranked
        print(json.dumps(rows, indent=2))
        return 0

    print_table(ranked, args.top)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
