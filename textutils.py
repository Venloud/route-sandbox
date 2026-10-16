"""Small text helpers."""
import re


def slugify(text: str) -> str:
    """Lowercase, replace non-alphanumerics with single hyphens, strip edges."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate(text: str, max_len: int, suffix: str = "…") -> str:
    """Return text cut to at most max_len characters, ending with suffix if cut."""
    if isinstance(max_len, bool) or not isinstance(max_len, int):
        raise TypeError("max_len must be an int")
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    if len(text) <= max_len:
        return text
    if max_len < len(suffix):
        return suffix[:max_len]
    return text[: max_len - len(suffix)] + suffix
