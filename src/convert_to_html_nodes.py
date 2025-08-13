from convert_to_blocks import *
from convert_to_block_type import *
from obj_htmlnode import *

def convert_to_html_node(markdown):
    blocks = convert_to_blocks(markdown)
    for block in blocks:
        block_type = convert_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            pass