import os

from convert_markdown_to_html_node import *
from extract_markdown_title import *

def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    with open(from_path) as from_path_file:
        markdown = from_path_file.read()

    with open(template_path) as template_path_file:
        template = template_path_file.read()

    #from_path.close()
    #template_path.close()

    title = extract_markdown_title(markdown)    
    html = convert_markdown_to_html_node(markdown)    
    content = html.to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    print(template)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(dest_path)
    with open(dest_path + "index.html", "w") as index:
        index.write(template)
