
def extract_markdown_title(markdown):
    header = markdown.split("\n")
    if not header[0].startswith("# "):
        raise Exception(f"'{header[0]}' not a valid h1 header!")
    header = header[0].strip("\n")
    header = header[2:]
    return header

    