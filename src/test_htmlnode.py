import unittest

from obj_htmlnode import *

class TestHTMLNode(unittest.TestCase):

	def test_to_html(self):
		test_A = HTMLNode("<a>","Text in a paragraph", None, {"href": "https://www.google.com"})
		try:
			test_A.to_html()
		except NotImplementedError as error:
			print("Expecting Super() to_html:", error)

	def test_props_to_html(self):
		test_B = HTMLNode()
		test_A = HTMLNode("<a>","Text in a paragraph", [test_B], {"href": "https://www.google.com", "target": "_blank"})
		result_A = test_A.props_to_html()
		result_B = test_B.props_to_html()
		self.assertEqual(result_A, "href=\"https://www.google.com\" target=\"_blank\"")
		self.assertEqual(result_B, None)

	def test_repr(self):
		test_B = HTMLNode()
		test_A = HTMLNode("<a>","Text in a paragraph", [test_B], {"href": "https://www.google.com", "target": "_blank"})
		self.assertEqual(repr(test_A), "HTMLNode(<a>, Text in a paragraph, [HTMLNode(None, None, None, None)], {'href': 'https://www.google.com', 'target': '_blank'})")
		self.assertEqual(repr(test_B), "HTMLNode(None, None, None, None)")

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, link!", {"href": "https://www.google.com"})
		self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Hello, link!</a>")
	
	def test_leaf_to_html_missing_value(self):
		try:
			node = LeafNode("a", None, {"href": "https://www.google.com"})
			node.to_html()
		except ValueError as error:
			print("Expecting missing value:", error)

	def test_leaf_to_html_missing_tag(self):
		node = LeafNode(None, "Hello, link!")
		self.assertEqual(node.to_html(), "Hello, link!")

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_several_children(self):
		grandchild_node_1 = LeafNode("b", "grandchild")
		grandchild_node_2 = LeafNode("i", "grandchild")
		child_node = ParentNode("span", [grandchild_node_1])
		child_node_2 = ParentNode("span", [grandchild_node_2])
		parent_node = ParentNode("div", [child_node_2, child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><i>grandchild</i></span><span><b>grandchild</b></span></div>",
		)
	
	def test_to_html_with_no_tag(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode(None, [child_node])
		try:
			self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
		except ValueError as error:
			print("Expecting no tag:", error)

	def test_to_html_with_no_children(self):
		try:
			child_node = LeafNode("span", "child")
			parent_node = ParentNode("div", None)
			self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
		except ValueError as error:
			print("Expecting no children:", error)

if __name__ == "__main__":
	unittest.main()