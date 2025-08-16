from deploy_static_to_public import *
from generate_page_recursive import *

def main():
    deploy_static_to_public()
    dir_path_cont = "../porter/content/"
    template_path = "../porter/template.html"
    dir_path_dest = "../porter/public/"
    generate_page_recursive(dir_path_cont, template_path, dir_path_dest)

main()