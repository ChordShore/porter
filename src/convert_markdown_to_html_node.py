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
            lines = block.split("\n")
            lines = " ".join(lines)
            children = convert_text_to_children(lines)
            node = ParentNode("p", children)
            child_nodes.append(node)

        if block_type == BlockType.HEADING:
            hash_count = 0
            for char in block:
                if char == "#":
                    hash_count += 1
                else:
                    break
            if hash_count > 6:
                raise ValueError("Invalid Heading Level!")
            line = block[hash_count + 1 : ]
            children = convert_text_to_children(line)
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
            lines = block.split("\n")
            quote_lines = []
            for line in lines:
                if line.startswith(">") is False:
                    raise ValueError("Invalid Quote Block")
                quote_lines.append(line.lstrip(">").strip())
            text = " ".join(quote_lines)
            children = convert_text_to_children(text)
            node = ParentNode("blockquote", children)
            child_nodes.append(node)
        
        if block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            children = []
            for line in lines:
                text = line[2:]
                list_children = convert_text_to_children(text)
                children.append(ParentNode("li", list_children))
            node = ParentNode("ul", children)
            child_nodes.append(node)
        
        if block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            children = []
            for line in lines:
                text = line[3:]
                list_children = convert_text_to_children(text)
                children.append(ParentNode("li", list_children))
            node = ParentNode("ol", children)
            child_nodes.append(node)

    parent_node = ParentNode("div", child_nodes)
    return parent_node