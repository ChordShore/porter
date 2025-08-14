import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def convert_block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

#if re.findall(r"((#{1,6} )[^\n]+\n)", lines[0]):
#    return BlockType.HEADING
#if re.findall(r"((``` )[\s\w]+( ```))", lines[0]):
#    return BlockType.CODE
#if re.findall(r"((>)[\s\w]+\n)+((>)[^\n]+)", lines[0]):
#    return BlockType.QUOTE
#if re.findall(r"((- )[\s\w]+\n)+((- )[^\n]+)", lines[0]):
#    return BlockType.UNORDERED_LIST
#if re.findall(r"((\d. )[\s\w]+\n)+((\d. )[^\n]+)", lines[0]):
#    return BlockType.ORDERED_LIST