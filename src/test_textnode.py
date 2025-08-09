import unittest

from textnode import TextNode, TextType

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
        print(repr(test_A))
        print(repr(test_B))

if __name__ == "__main__":
    unittest.main()