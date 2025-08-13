import unittest

from convert_to_text_nodes import *

class TestConvertToTextNode(unittest.TestCase):

	def test_convert_to_text_nodes(self):
		text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		
		new_nodes = text_to_textnodes(text)
		self.assertEqual(new_nodes, [
			TextNode("This is ", TextType.TEXT),
			TextNode("text", TextType.BOLD),
			TextNode(" with an ", TextType.TEXT),
			TextNode("italic", TextType.ITALIC),
			TextNode(" word and a ", TextType.TEXT),
			TextNode("code block", TextType.CODE),
			TextNode(" and an ", TextType.TEXT),
			TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
			TextNode(" and a ", TextType.TEXT),
			TextNode("link", TextType.LINK, "https://boot.dev"),
			])

if __name__ == "__main__":
	unittest.main()