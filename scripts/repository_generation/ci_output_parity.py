"""CI-only comparison of the public example's actual generated files."""
import argparse
from hashlib import sha256
from pathlib import Path
import sys

from .profile import ARTIFACTS


def read_documents(directory: Path) -> dict[str, bytes]:
    if set(p.name for p in directory.iterdir()) != set(ARTIFACTS):
        raise ValueError(f"{directory}: expected exactly {', '.join(ARTIFACTS)}")
    documents = {}
    for name in ARTIFACTS:
        path = directory / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"{path}: expected regular file")
        content = path.read_bytes()
        content.decode("utf-8")
        if b"\r" in content or not content.endswith(b"\n"):
            raise ValueError(f"{path}: expected UTF-8/LF document")
        documents[name] = content
    return documents


def compare(ubuntu: Path, windows: Path) -> int:
    try:
        left, right = read_documents(ubuntu), read_documents(windows)
    except (OSError, ValueError) as exc:
        print(f"Unable to compare generated documents: {exc}", file=sys.stderr)
        return 2
    mismatch = False
    for name in ARTIFACTS:
        equal = left[name] == right[name]
        mismatch |= not equal
        print(f"{name}: {'MATCH' if equal else 'MISMATCH'}")
        print(f"  Ubuntu SHA-256: {sha256(left[name]).hexdigest()}")
        print(f"  Windows SHA-256: {sha256(right[name]).hexdigest()}")
    if mismatch:
        print("Generated-document parity failed.", file=sys.stderr)
        return 1
    print("Generated-document parity passed: exactly two byte-identical documents.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ubuntu", type=Path)
    parser.add_argument("windows", type=Path)
    args = parser.parse_args()
    return compare(args.ubuntu, args.windows)


if __name__ == "__main__":
    raise SystemExit(main())
