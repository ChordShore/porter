import unittest

from obj_textnode import *
from convert_text_node_to_html_node import *

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_noteq(self):
		test_A = TextNode("test a", TextType.BOLD)
		test_B = TextNode("test b", TextType.LINK, "https://www.google.com/")
		self.assertNotEqual(test_A, test_B)

	def test_url_noteq(self):
		test_B = TextNode("test b", TextType.LINK, "https://www.google.com/")
		test_D = TextNode("test b", TextType.LINK, "https://www.youtube.com/")
		self.assertNotEqual(test_B, test_D)

	def test_varname_eq(self):
		test_A = TextNode("test a", TextType.BOLD)
		test_C = TextNode("test a", TextType.BOLD)
		self.assertEqual(test_A, test_C)

	def test_repr(self):
		test_A = TextNode("test a", TextType.BOLD)
		test_B = TextNode("test b", TextType.LINK, "https://www.google.com/")
		self.assertEqual(repr(test_A), "TextNode(test a, bold_text, None)")
		self.assertEqual(repr(test_B), "TextNode(test b, link, https://www.google.com/)")

	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = convert_text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_bold(self):
		node = TextNode("This is a text node", TextType.BOLD)
		html_node = convert_text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a text node")

	def test_italic(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		html_node = convert_text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is a text node")

	def test_code(self):
		node = TextNode("This is a text node", TextType.CODE)
		html_node = convert_text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "This is a text node")

	def test_link(self):
		node = TextNode("This is a text node", TextType.LINK, "https://www.google.com/")
		html_node = convert_text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is a text node")
		self.assertEqual(html_node.props, {"href": f"{node.url}"})

	def test_image(self):
		node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com/")
		html_node = convert_text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {"src": f"{node.url}", "alt": f"{node.text}"})

	def test_invalid(self):
		try:
			node = TextNode("This is a text node", TextType.INVALID, "https://www.google.com/")
			html_node = convert_text_node_to_html_node(node)
		except AttributeError as error:
			print("Expected:", error)

if __name__ == "__main__":
	unittest.main()