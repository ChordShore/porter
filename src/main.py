from deploy_static_to_public import *
from generate_page import *

def main():
    deploy_static_to_public()
    from_path = "../porter/content/index.md"
    template_path = "../porter/template.html"
    dest_path = "../porter/public/"
    generate_page(from_path, template_path, dest_path)

main()