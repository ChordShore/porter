import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def test_to_html(self):
        test_A = HTMLNode("<a>","Text in a paragraph", None, {"href": "https://www.google.com"})
        try:
            test_A.to_html()
        except NotImplementedError:
            print("to_HTML function Not Implemented!")

    def test_props_to_html(self):
        test_B = HTMLNode()
        test_A = HTMLNode("<a>","Text in a paragraph", [test_B], {"href": "https://www.google.com", "target": "_blank"})
        result_A = test_A.props_to_html()
        result_B = test_B.props_to_html()
        self.assertEqual(result_A, "href=\"https://www.google.com\" target=\"_blank\" ")
        self.assertEqual(result_B, None)

    def test_repr(self):
        test_B = HTMLNode()
        test_A = HTMLNode("<a>","Text in a paragraph", [test_B], {"href": "https://www.google.com", "target": "_blank"})
        print(repr(test_A))
        print(repr(test_B))

if __name__ == "__main__":
    unittest.main()