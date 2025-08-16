import sys

from deploy_static_to_public import *
from generate_page_recursive import *

def main():

    basepath = sys.argv[0]
    if basepath is None:
        basepath = "/"

    deploy_static_to_public()
    dir_path_cont = "../porter/content/"
    template_path = "../porter/template.html"
    dir_path_dest = "../porter/docs/"
    generate_page_recursive(dir_path_cont, template_path, dir_path_dest, basepath)

    #print(basepath)

main()