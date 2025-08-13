from obj_textnode import *
from extract_markdown_images import *

def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		found_images = extract_markdown_images(node.text)
		if len(found_images) < 1:
			new_nodes.append(node)
			continue
		temp_node_text = node.text

		for image in found_images:
			split_text = temp_node_text.split(f"![{image[0]}]({image[1]})", 1)
			if len(split_text) != 2:
				raise ValueError("Closing image syntax not found, invalid Markdown syntax!")				
			if split_text[0] != "":
				new_nodes.append(TextNode(split_text[0], TextType.TEXT))
			new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
			temp_node_text = split_text[1]
		if temp_node_text != "":
			new_nodes.append(TextNode(temp_node_text, TextType.TEXT))		

	return new_nodes