import sys

from deploy_static_to_public import *
from generate_page_recursive import *

dir_path_cont = "./content/"
template_path = "./template.html"
dir_path_dest = "./docs/"
default_basepath = "/"

def main():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    deploy_static_to_public()
    generate_page_recursive(dir_path_cont, template_path, dir_path_dest, basepath)

main()