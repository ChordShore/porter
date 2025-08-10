from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type is not TextType.TEXT:
			new_nodes.append(node)
		else:
			new_text_list = node.text.split(delimiter)
			if len(new_text_list) % 2 == 0:
				raise ValueError("Closing delimiter not found, invalid Markdown syntax!")
			else:
				for i in range(len(new_text_list)):
					if new_text_list[i] == "":
						continue
					if i % 2 != 0:
						new_nodes.append(TextNode(new_text_list[i], text_type))
					else:
						new_nodes.append(TextNode(new_text_list[i], TextType.TEXT))
	return new_nodes