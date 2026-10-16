# Changelog

## Unreleased

- Add `truncate(text, max_len, suffix="…")`, which never exceeds `max_len` including the suffix, trims the suffix when `max_len` is smaller, and raises `ValueError` for negative `max_len`.
- Initial sandbox.
