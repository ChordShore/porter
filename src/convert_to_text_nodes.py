from obj_textnode import *
from split_nodes_delimiter import *
from split_nodes_link import *
from split_nodes_image import *

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    debold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    decode_nodes = split_nodes_delimiter(debold_nodes, "`", TextType.CODE)
    deital_nodes = split_nodes_delimiter(decode_nodes, "_", TextType.ITALIC)
    deimag_nodes = split_nodes_image(deital_nodes)
    delink_nodes = split_nodes_link(deimag_nodes)
    return delink_nodes