from obj_textnode import *
from extract_markdown_links import *

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		found_links = extract_markdown_links(node.text)
		if len(found_links) < 1:
			new_nodes.append(node)
			continue
		temp_node_text = node.text

		for link in found_links:
			split_text = temp_node_text.split(f"[{link[0]}]({link[1]})", 1)
			if len(split_text) != 2:
				raise ValueError("Closing link syntax not found, invalid Markdown syntax!")
			if split_text[0] != "":
				new_nodes.append(TextNode(split_text[0], TextType.TEXT))
			new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
			temp_node_text = split_text[1]
		if temp_node_text != "":
			new_nodes.append(TextNode(temp_node_text, TextType.TEXT))	

	return new_nodes