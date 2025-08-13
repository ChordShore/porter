import unittest

from convert_to_blocks import *

class TestConvertToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = convert_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_with_newlines(self):
        md = """

test


"""
        blocks = convert_to_blocks(md)
        self.assertEqual(blocks, ["test"])

if __name__ == "__main__":
	unittest.main()