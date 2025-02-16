from textnode import TextNode
from textnode import TextType


def main():
    text = "This is a text node"
    text_type = TextType("bold")
    url = "https://www.boot.dev"
    text_node = TextNode(text, text_type, url)
    print(text_node)


main()
