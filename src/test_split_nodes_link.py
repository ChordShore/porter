import unittest

from obj_textnode import *
from split_nodes_link import *

class TestSplitNodesLink(unittest.TestCase):

	def test_split_nodes_link(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a link ", TextType.TEXT),
				TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
				TextNode(" and ", TextType.TEXT),
				TextNode(
					"to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
					),
			],
			new_nodes,
		)

if __name__ == "__main__":
	unittest.main()