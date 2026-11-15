"""Compare complete Validator Component catalog snapshots from Ubuntu and Windows CI.

This compares catalog data, not filesystem paths from validation diagnostics.
"""

import argparse
import json
import sys
from pathlib import Path


REQUIRED_DETAIL_FIELDS = (
    "path", "id", "name", "version", "status", "metadata_status",
    "metadata_sha256", "content_sha256",
)


def read_catalog(path: Path) -> dict:
    """Load a complete catalog, rejecting truncated or partial inventories."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected JSON object")
    components = data.get("components")
    details = data.get("details")
    scope = data.get("scope")
    if (
        not isinstance(components, list) or not components
        or not all(isinstance(item, str) and item for item in components)
        or len(set(components)) != len(components)
        or not isinstance(details, list)
        or len(details) != len(components)
        or type(data.get("count")) is not int
        or data["count"] != len(components)
        or "pagination" in data
    ):
        raise ValueError(f"{path}: expected a complete, non-paginated catalog")
    if (
        not isinstance(scope, dict)
        or not isinstance(scope.get("families"), list)
        or not scope["families"]
        or not all(
            isinstance(family, str) and family in ("readme", "documentation", "workflow")
            for family in scope["families"]
        )
        or len(set(scope["families"])) != len(scope["families"])
    ):
        raise ValueError(f"{path}: missing or invalid catalog family scope")
    for component, detail in zip(components, details):
        if not isinstance(detail, dict) or detail.get("path") != component:
            raise ValueError(f"{path}: catalog detail order/path mismatch")
        for field in REQUIRED_DETAIL_FIELDS:
            if field not in detail:
                raise ValueError(f"{path}: missing detail field {field} for {component}")
        for field in ("metadata_sha256", "content_sha256"):
            value = detail[field]
            if (
                not isinstance(value, str) or len(value) != 64
                or any(char not in "0123456789abcdef" for char in value)
            ):
                raise ValueError(f"{path}: invalid {field} for {component}")
    return data



def describe_mismatches(left: dict, right: dict, limit: int = 10) -> str:
    """Summarize which fields differ without printing large catalog contents."""
    differences = []
    if left["components"] != right["components"]:
        differences.append("Component path inventory/order")
    left_details = {entry["path"]: entry for entry in left["details"]}
    right_details = {entry["path"]: entry for entry in right["details"]}
    for path in sorted(set(left_details) | set(right_details)):
        before, after = left_details.get(path), right_details.get(path)
        if before is None or after is None:
            differences.append(f"{path}: missing Component details")
        elif before != after:
            fields = sorted(
                key for key in set(before) | set(after)
                if (key in before) != (key in after)
                or before.get(key) != after.get(key)
            )
            differences.append(f"{path}: {', '.join(fields)}")
    for key in sorted(set(left) | set(right)):
        if key not in ("components", "details") and (
            (key in left) != (key in right)
            or left.get(key) != right.get(key)
        ):
            differences.append(f"catalog field: {key}")
    shown = differences[:limit]
    if len(differences) > limit:
        shown.append(f"... and {len(differences) - limit} more differences")
    return "; ".join(shown)


def compare_catalogs(ubuntu: Path, windows: Path) -> int:
    """Return zero only if both checked-out Component catalogs match exactly."""
    try:
        left = read_catalog(ubuntu)
        right = read_catalog(windows)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"Unable to compare Component catalogs: {exc}", file=sys.stderr)
        return 2
    if left != right:
        print(
            "Component catalogs differ between Ubuntu and Windows. "
            + describe_mismatches(left, right),
            file=sys.stderr,
        )
        return 1
    print(
        f"Component catalog parity passed: {left['count']} Components and their "
        "metadata/content SHA-256 digests match on Ubuntu and Windows."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare full Ubuntu and Windows Component catalog artifacts."
    )
    parser.add_argument("ubuntu", type=Path)
    parser.add_argument("windows", type=Path)
    args = parser.parse_args()
    return compare_catalogs(args.ubuntu, args.windows)


if __name__ == "__main__":
    raise SystemExit(main())
