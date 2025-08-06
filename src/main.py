from textnode import *

def main():
    print("hello world")
    test_A = TextNode("test a", TextType.BOLD_TEXT)
    test_B = TextNode("test b", TextType.LINK, "https://www.chordshore.com/")
    test_C = TextNode("test a", TextType.BOLD_TEXT)
    test_D = TextNode("test b", TextType.LINK, "https://www.youtube.com/")

    print(repr(test_A))
    print(repr(test_B))
    print(test_A == test_B)
    print(test_A == test_C)
    print(test_B == test_D)

main()