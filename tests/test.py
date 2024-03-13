import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "")))
from convert import convert_to_comment


class TestConvertToComment(unittest.TestCase):
    def test_single_line(self):
        content = "This is a single line comment"
        expected = "// This is a single line comment"
        self.assertEqual(convert_to_comment(content), expected)

    def test_empty_line(self):
        content = ""
        expected = "//"
        self.assertEqual(convert_to_comment(content), expected)

    def test_multiple_lines(self):
        content = "First line\nSecond line"
        expected = "// First line\n// Second line"
        self.assertEqual(convert_to_comment(content), expected)

    def test_line_break(self):
        content = "First line\n\nSecond line"
        expected = "// First line\n//\n// Second line"
        self.assertEqual(convert_to_comment(content), expected)


def test_long_line(self):
    content = "This is a very long line that should be split into multiple lines because its length is more than 80 characters, which is the maximum allowed line length."
    expected = "// This is a very long line that should be split into multiple lines because its\n// length is more than 80 characters, which is the maximum allowed line length."
    self.assertEqual(convert_to_comment(content), expected)


if __name__ == "__main__":
    unittest.main()
