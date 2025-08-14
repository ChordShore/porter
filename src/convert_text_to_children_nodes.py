from obj_htmlnode import *
from convert_text_to_text_node import *
from convert_text_node_to_html_node import *

def convert_text_to_children(block):

    lines = block.split("\n")
    line_parse = []
    for i in range(len(lines)):
        if lines[i] != lines[-1]:
            lines[i] += " "
        line_parse.append(convert_text_to_text_node(lines[i]))
    children = []
    for line in line_parse:
        for text_node in line:
            children.append(convert_text_node_to_html_node(text_node))

    return children