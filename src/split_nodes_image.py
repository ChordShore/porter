from obj_textnode import *

def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
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