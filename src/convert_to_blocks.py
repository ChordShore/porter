
def convert_to_blocks(markdown):
    newline_blocks = markdown.split("\n\n")
    result_blocks = []
    for block in newline_blocks:
        block = block.strip()
        if block != '':
            result_blocks.append(block)
    return result_blocks