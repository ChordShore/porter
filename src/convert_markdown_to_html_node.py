from obj_htmlnode import *
from convert_markdown_to_blocks import *
from convert_block_to_block_type import *
from convert_text_to_text_node import *
from convert_text_node_to_html_node import *
from convert_text_to_children_nodes import *

def convert_markdown_to_html_node(markdown):
    blocks = convert_markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = convert_block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children = convert_text_to_children(block)
            node = ParentNode("p", children)
            child_nodes.append(node)

        if block_type == BlockType.HEADING:
            hash_count = 0
            for char in block:
                if char == "#":
                    hash_count += 1
            children = convert_text_to_children(block)
            node = ParentNode(f"h{hash_count}", children)
            child_nodes.append(node)

        if block_type == BlockType.CODE:
            block = block.lstrip("```\n")
            block = block.rstrip("```")
            text_node = TextNode(block, TextType.CODE)
            child = convert_text_node_to_html_node(text_node)
            node = ParentNode("pre", [child])
            child_nodes.append(node)

        if block_type == BlockType.QUOTE:
            children = convert_text_to_children(block)
            node = ParentNode("blockquote", children)
            child_nodes.append(node)
        
        if block_type == BlockType.UNORDERED_LIST:
            children = convert_text_to_children(block)
            node = ParentNode("", children)
            child_nodes.append(node)
        
        if block_type == BlockType.ORDERED_LIST:
            children = convert_text_to_children(block)
            node = ParentNode("", children)
            child_nodes.append(node)

    parent_node = ParentNode("div", child_nodes)
    return parent_node

    