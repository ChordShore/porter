from obj_textnode import *
from obj_htmlnode import *

def convert_text_node_to_html_node(text_node):
    type = text_node.text_type
    if type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise AttributeError("Text Node type not found!")