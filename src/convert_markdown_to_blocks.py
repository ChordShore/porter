
def convert_markdown_to_blocks(markdown):
    newline_blocks = markdown.split("\n\n")
    result_blocks = []
    for block in newline_blocks:
        if block == '':
            continue
        block = block.strip()
        result_blocks.append(block)
    return result_blocks