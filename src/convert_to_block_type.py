import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def convert_to_block_type(block):
    if re.findall(r"((#{1,6} )[^\n]+\n)", block):
        return BlockType.HEADING
    if re.findall(r"((``` )[\s\w]+( ```))", block):
        return BlockType.CODE
    if re.findall(r"((>)[\s\w]+\n)+((>)[^\n]+)", block):
        return BlockType.QUOTE
    if re.findall(r"((- )[\s\w]+\n)+((- )[^\n]+)", block):
        return BlockType.UNORDERED_LIST
    if re.findall(r"((\d. )[\s\w]+\n)+((\d. )[^\n]+)", block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH