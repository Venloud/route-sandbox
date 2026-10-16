"""Small text helpers."""
import re


def slugify(text: str) -> str:
    """Lowercase, replace non-alphanumerics with single hyphens, strip edges."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
