#!/usr/bin/env python3
"""Save immutable HTML proposal snapshots and update a manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


VERSION_RE = re.compile(r"^v?(\d+)$")
SNAPSHOT_RE = re.compile(r"proposal_v(\d+)\.html$")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"schema_version": 1, "versions": []}
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if "versions" not in data or not isinstance(data["versions"], list):
        raise ValueError(f"Invalid manifest: {path}")
    return data


def normalize_version(raw: str) -> str:
    match = VERSION_RE.match(raw.strip())
    if not match:
        raise ValueError("Version must be an integer, v001, v002, etc.")
    return f"v{int(match.group(1)):03d}"


def next_version(versions_dir: Path, manifest: dict) -> str:
    highest = 0
    for entry in manifest.get("versions", []):
        version = str(entry.get("version", ""))
        match = VERSION_RE.match(version)
        if match:
            highest = max(highest, int(match.group(1)))
    if versions_dir.exists():
        for path in versions_dir.iterdir():
            match = SNAPSHOT_RE.match(path.name)
            if match:
                highest = max(highest, int(match.group(1)))
    return f"v{highest + 1:03d}"


def write_manifest(path: Path, manifest: dict) -> None:
    tmp_path = path.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")
    tmp_path.replace(path)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy an HTML proposal artifact into versions/ and update manifest.json."
    )
    parser.add_argument("session_dir", help="Proposal review session directory.")
    parser.add_argument("html_path", help="HTML artifact to snapshot.")
    parser.add_argument("--label", default="", help="Short version label.")
    parser.add_argument("--notes", default="", help="Optional version notes.")
    parser.add_argument("--version", default="", help="Optional explicit version such as v003.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    session_dir = Path(args.session_dir).expanduser().resolve()
    html_path = Path(args.html_path).expanduser()
    if not html_path.is_absolute():
        html_path = (Path.cwd() / html_path).resolve()

    if not html_path.exists():
        print(f"HTML artifact not found: {html_path}", file=sys.stderr)
        return 2
    if html_path.suffix.lower() not in {".html", ".htm"}:
        print(f"Expected an HTML file, got: {html_path}", file=sys.stderr)
        return 2

    versions_dir = session_dir / "versions"
    versions_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = versions_dir / "manifest.json"
    manifest = load_manifest(manifest_path)

    version = normalize_version(args.version) if args.version else next_version(versions_dir, manifest)
    dest = versions_dir / f"proposal_{version}.html"
    if dest.exists():
        print(f"Version already exists: {dest}", file=sys.stderr)
        return 2

    shutil.copy2(html_path, dest)
    entry = {
        "version": version,
        "file": str(dest.relative_to(session_dir)),
        "source": str(html_path),
        "label": args.label,
        "notes": args.notes,
        "sha256": sha256_file(dest),
        "timestamp_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }
    manifest.setdefault("schema_version", 1)
    manifest.setdefault("versions", []).append(entry)
    write_manifest(manifest_path, manifest)
    print(json.dumps(entry, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
