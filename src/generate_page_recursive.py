import os, shutil

from extract_markdown_title import *
from convert_markdown_to_html_node import *

def generate_page_recursive(dir_path_content, template_path, dir_path_dest):
    print(f"Generating page from {dir_path_content} to {dir_path_dest} using {template_path}.")
    
    file_list = os.listdir(dir_path_content)
    for file in file_list:
        
        file_name = file.split(".")
        content_copy_path = os.path.join(dir_path_content, file)
        public_copy_path = os.path.join(dir_path_dest, f"{file_name[0]}")
        
        if os.path.isfile(content_copy_path):

            with open(content_copy_path) as content_copy_file:
                markdown = content_copy_file.read()

            with open(template_path) as template_file:
                template = template_file.read()

            title = extract_markdown_title(markdown)    
            html = convert_markdown_to_html_node(markdown)    
            content = html.to_html()
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", content)

            if not os.path.exists(os.path.dirname(public_copy_path)):
                os.makedirs(public_copy_path)
            with open(public_copy_path + ".html", "w") as file_write:
                file_write.write(template)
        elif os.path.isdir(content_copy_path):
            os.mkdir(public_copy_path)
            generate_page_recursive(content_copy_path, template_path, public_copy_path)