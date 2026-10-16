import unittest

from textutils import slugify, truncate


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")


class TruncateTests(unittest.TestCase):
    def assert_truncated(self, text, max_len, expected, suffix="…"):
        result = truncate(text, max_len, suffix)
        self.assertEqual(result, expected)
        self.assertLessEqual(len(result), max_len)

    def test_unchanged_text(self):
        text = "  keep\t\n"
        self.assertEqual(truncate(text, len(text)), text)
        self.assertEqual(truncate(text, len(text) + 1), text)

    def test_truncation(self):
        self.assert_truncated("x", 1, "x", "...")
        self.assert_truncated("abcdef", 4, "abc…")
        self.assert_truncated("abcdefgh", 5, "ab...", "...")
        self.assert_truncated("abcdef", 2, "..", "...")
        self.assert_truncated("abcdef", 3, "...", "...")
        self.assert_truncated("abcdef", 3, "abc", "")
        self.assert_truncated("abc", 0, "")
        self.assert_truncated("", 0, "")
        self.assert_truncated("xéz", 3, "xe…")

    def test_negative_max_len(self):
        with self.assertRaises(ValueError):
            truncate("a", -1)

    def test_max_len_must_be_an_int(self):
        for max_len in (True, False, 2.0, "2", None):
            with self.subTest(max_len=max_len):
                with self.assertRaises(TypeError):
                    truncate("a", max_len)


if __name__ == "__main__":
    unittest.main()
