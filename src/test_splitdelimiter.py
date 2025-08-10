import unittest

from textnode import *
from splitdelimiter import *

class TestSplitDelimiter(unittest.TestCase):

	def test_text(self):
		node = TextNode("This is text", TextType.TEXT)
		try:
			new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		except ValueError as error:
			print("Expected:", error)

	def test_bold(self):
		node = TextNode("This is **a** text node", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertEqual(new_nodes, [
			TextNode("This is ", TextType.TEXT),
			TextNode("a", TextType.BOLD),
			TextNode(" text node", TextType.TEXT),
		])

	def test_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(new_nodes, [
			TextNode("This is text with a ", TextType.TEXT),
			TextNode("code block", TextType.CODE),
			TextNode(" word", TextType.TEXT),
		])

	def test_delim_bold(self):
		node = TextNode("This is text with a **bolded** word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

    #Below Unit Tests from the Boot.dev solution files
	def test_delim_bold_double(self):
		node = TextNode(
			"This is text with a **bolded** word and **another**", TextType.TEXT
		)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded", TextType.BOLD),
				TextNode(" word and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_bold_multiword(self):
		node = TextNode(
			"This is text with a **bolded word** and **another**", TextType.TEXT
		)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("bolded word", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("another", TextType.BOLD),
			],
			new_nodes,
		)

	def test_delim_italic(self):
		node = TextNode("This is text with an _italic_ word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

	def test_delim_bold_and_italic(self):
		node = TextNode("**bold** and _italic_", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
		self.assertListEqual(
			[
				TextNode("bold", TextType.BOLD),
				TextNode(" and ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
			],
			new_nodes,
		)

	def test_delim_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" word", TextType.TEXT),
			],
			new_nodes,
		)

if __name__ == "__main__":
	unittest.main()