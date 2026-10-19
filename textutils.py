"""Small text helpers."""
import re
import unicodedata


def slugify(text: str) -> str:
    """Lowercase, replace non-alphanumerics with single hyphens, strip edges."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate(text: str, max_len: int, suffix: str = "…") -> str:
    """Count lengths in code points after NFC normalization; append suffix if cut."""
    if isinstance(max_len, bool) or not isinstance(max_len, int):
        raise TypeError("max_len must be an int")
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    text = unicodedata.normalize("NFC", text)
    suffix = unicodedata.normalize("NFC", suffix)
    if len(text) <= max_len:
        return text
    if max_len < len(suffix):
        return suffix[:max_len]
    return text[: max_len - len(suffix)] + suffix
