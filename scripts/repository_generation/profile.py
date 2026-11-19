"""The explicitly supported text-only generation profile."""
from . import GenerationError

TEMPLATE_ID = "TPL-BACKEND"
TEMPLATE_VERSION = "0.1.0"
REQUIRED = (
    ("README-HERO", "1.0.0", "readme/hero"),
    ("README-OVERVIEW", "1.0.0", "readme/overview"),
    ("README-FEATURES", "1.0.0", "readme/features"),
    ("README-TECH-STACK", "1.0.0", "readme/tech-stack"),
    ("README-QUICK-START", "1.0.0", "readme/quick-start"),
    ("README-DOCUMENTATION", "1.0.0", "readme/documentation"),
    ("README-FOOTER", "1.0.0", "readme/footer"),
    ("DOC-CHANGELOG", "0.1.0", "documentation/changelog"),
)
ARTIFACTS = ("README.md", "CHANGELOG.md")
CATEGORIES = ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security")
VISUAL_LIMITATION = "README-HERO requires conceptual VCL-HERO 1.0.0; text-only profile, not full Template conformance."


def require_profile(template_id: str, version: str) -> None:
    if (template_id, version) != (TEMPLATE_ID, TEMPLATE_VERSION):
        raise GenerationError(f"unsupported Template: {template_id} {version}")
