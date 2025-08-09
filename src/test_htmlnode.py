import unittest

from htmlnode import *

class TestTextNode(unittest.TestCase):

    def test_to_html(self):
        test_A = HTMLNode("<a>","Text in a paragraph", None, {"href": "https://www.google.com"})
        try:
            test_A.to_html()
        except NotImplementedError:
            print("Parent to_HTML function Not Implemented")

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
        print(repr(test_A))
        print(repr(test_B))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, link!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Hello, link!</a>")
    
    def test_leaf_to_html_missing_value(self):
        try:
            node = LeafNode("a", None, {"href": "https://www.google.com"})
        except ValueError:
            print("LeafNode requires a value")

    def test_leaf_to_html_missing_tag(self):
        node = LeafNode(None, "Hello, link!")
        self.assertEqual(node.to_html(), "Hello, link!")

if __name__ == "__main__":
    unittest.main()