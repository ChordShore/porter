import unittest

from convert_block_to_block_type import *

class TestConvertToBlockType(unittest.TestCase):

    def test_convert_heading_to_block_type(self):
        md = '''# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6'''
        result = convert_block_to_block_type(md)
        self.assertEqual(result, BlockType.HEADING)

    def test_convert_code_to_block_type(self):
        md = "```\ncode block\n```"
        result = convert_block_to_block_type(md)
        self.assertEqual(result, BlockType.CODE)

    def test_convert_quote_to_block_type(self):
        md = '''>quote
>quote
>quote'''
        result = convert_block_to_block_type(md)
        self.assertEqual(result, BlockType.QUOTE)

    def test_convert_unordered_list_to_block_type(self):
        md = '''- list
- list
- list'''
        result = convert_block_to_block_type(md)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_convert_ordered_list_to_block_type(self):
        md = '''1. list
2. list
3. list'''
        result = convert_block_to_block_type(md)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_convert_paragraph_to_block_type(self):
        md = '''hello world!
hello code!'''
        result = convert_block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

if __name__ == "__main__":
	unittest.main()