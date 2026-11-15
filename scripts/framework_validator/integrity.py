"""Read-only, deterministic digest helpers for Framework Components."""

import hashlib
import os
from pathlib import Path


def metadata_sha256(path: Path) -> str | None:
    """Hash the raw metadata bytes, returning None for unreadable or absent files."""
    if path.is_symlink() or path.parent.is_symlink():
        raise ValueError("metadata.yml or its Component root is a symbolic link")
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def component_content_sha256(component: Path) -> str:
    """Hash every regular Component file and its relative path, in stable order.

    Reject symbolic links, including links to directories, instead of following
    potentially external content. The framing prevents path/content ambiguity.
    """
    if component.is_symlink():
        raise ValueError("Component root is a symbolic link")
    if not component.is_dir():
        raise ValueError("Component root is not a directory")

    digest = hashlib.sha256()
    files = []

    def fail_on_walk_error(error: OSError) -> None:
        raise error

    for directory, directories, filenames in os.walk(
        component, followlinks=False, onerror=fail_on_walk_error
    ):
        parent = Path(directory)
        for name in directories + filenames:
            entry = parent / name
            if entry.is_symlink():
                raise ValueError(
                    f"Component content contains symbolic link: {entry.relative_to(component).as_posix()}"
                )
        for name in filenames:
            entry = parent / name
            if not entry.is_file():
                raise ValueError(
                    f"Component content contains non-regular file: {entry.relative_to(component).as_posix()}"
                )
            files.append(entry)
    for path in sorted(files, key=lambda item: item.relative_to(component).as_posix()):
        relative = path.relative_to(component).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        with path.open("rb") as stream:
            before = os.fstat(stream.fileno())
            digest.update(before.st_size.to_bytes(8, "big"))
            bytes_read = 0
            while chunk := stream.read(65536):
                digest.update(chunk)
                bytes_read += len(chunk)
            after = os.fstat(stream.fileno())
            if (
                bytes_read != before.st_size
                or after.st_size != before.st_size
                or after.st_mtime_ns != before.st_mtime_ns
            ):
                raise ValueError(
                    f"Component file changed during hashing: "
                    f"{path.relative_to(component).as_posix()}"
                )
    return digest.hexdigest()


