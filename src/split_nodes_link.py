from obj_textnode import *
from extract_markdown_links import *

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		found_links = extract_markdown_links(node.text)
		if len(found_links) < 1:
			new_nodes.append(node)
			continue

		new_text_list = []
		temp_node_text = node.text
		while len(temp_node_text) > 0:
			for link in found_links:
				if link[0] in temp_node_text:
					split_text = temp_node_text.split(f"[{link[0]}]({link[1]})", 1)
					new_text_list.append(split_text[0])
					new_text_list.append(link)
					if len(split_text) > 1:
						temp_node_text = split_text[1]
					else:
						break

		for i in range(len(new_text_list)):
			if new_text_list[i] == "":
				continue
			#print("New Text List: ", new_text_list[i])
			if new_text_list[i] in found_links:
				new_nodes.append(TextNode(new_text_list[i][0], TextType.LINK, new_text_list[i][1]))
			else:
				new_nodes.append(TextNode(new_text_list[i], TextType.TEXT))
				
	return new_nodes