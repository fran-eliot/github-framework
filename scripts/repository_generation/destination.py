"""Bounded local destination validation and exclusive document writing."""
from pathlib import Path
import re
import stat

from . import GenerationError
from .assembly import Document
from .profile import ARTIFACTS

_NAME = re.compile(r"[a-z](?:[a-z0-9-]{0,61}[a-z0-9])?")
_RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)),
             *(f"lpt{i}" for i in range(1, 10))}


class DestinationError(GenerationError):
    """Destination rejected or write failed; no automatic cleanup."""

    def __init__(self, message: str, incomplete_path: Path | None = None):
        self.incomplete_path = incomplete_path
        super().__init__(message)


def _linked(info):
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )


def _directory(path: Path) -> Path:
    """Inspect lexical ancestors before resolving; reject traversal and links."""
    if ".." in path.parts:
        raise DestinationError(f"parent traversal is not supported: {path}")
    absolute = path.absolute()
    if ".." in absolute.parts:
        raise DestinationError(f"parent traversal is not supported: {path}")
    for current in (*reversed(absolute.parents), absolute):
        try:
            info = current.lstat()
        except OSError as exc:
            raise DestinationError(f"unavailable output parent: {current}") from exc
        if _linked(info) or not stat.S_ISDIR(info.st_mode):
            raise DestinationError(f"linked or non-directory output ancestor: {current}")
    try:
        return absolute.resolve(strict=True)
    except OSError as exc:
        raise DestinationError(f"cannot resolve output parent: {path}") from exc


def validate_destination(root: Path, parent: Path, name: str) -> Path:
    """Read-only destination check; never create directories."""
    if not isinstance(name, str) or not _NAME.fullmatch(name) or name in _RESERVED:
        raise DestinationError("invalid portable output directory name")
    resolved_parent = _directory(parent)
    try:
        source = root.resolve(strict=True)
    except OSError as exc:
        raise DestinationError("cannot resolve Framework source root") from exc
    target = resolved_parent / name
    if resolved_parent.is_relative_to(source) or target.is_relative_to(source):
        raise DestinationError("output must be outside the Framework checkout")
    try:
        target.lstat()
    except FileNotFoundError:
        return target
    except OSError as exc:
        raise DestinationError(f"cannot inspect output destination: {target}") from exc
    raise DestinationError(f"output destination already exists: {target}")


def _check_documents(documents: tuple[Document, ...]) -> None:
    if tuple(doc.name for doc in documents) != ARTIFACTS:
        raise DestinationError("expected exactly README.md and CHANGELOG.md in order")
    for doc in documents:
        if not isinstance(doc.content, bytes) or not doc.content.endswith(b"\n") or b"\r" in doc.content:
            raise DestinationError(f"{doc.name}: expected LF document bytes")
        try:
            doc.content.decode("utf-8")
        except UnicodeError as exc:
            raise DestinationError(f"{doc.name}: invalid UTF-8") from exc


def _write_document(path: Path, content: bytes) -> None:
    with path.open("xb") as stream:
        if stream.write(content) != len(content):
            raise OSError("short write")


def write_documents(root: Path, parent: Path, name: str,
                    documents: tuple[Document, ...]) -> Path:
    """Create only a fresh child and its two fixed files.

    No deletion or recovery transaction. A failure after directory creation
    explicitly exposes the incomplete owned directory for manual inspection.
    Concurrent hostile path replacement is outside the supported model.
    """
    _check_documents(documents)
    target = validate_destination(root, parent, name)
    try:
        target.mkdir(exist_ok=False)
    except OSError as exc:
        raise DestinationError(f"cannot create output directory: {target}: {exc}") from exc
    try:
        for document in documents:
            _write_document(target / document.name, document.content)
        for document in documents:
            if (target / document.name).read_bytes() != document.content:
                raise OSError(f"written content mismatch: {document.name}")
    except OSError as exc:
        raise DestinationError(
            f"generation failed; inspect incomplete output at {target}: {exc}",
            incomplete_path=target,
        ) from exc
    return target
