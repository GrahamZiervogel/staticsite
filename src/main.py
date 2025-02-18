from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    text = "GOOGLE"
    text_type = TextType.LINK
    url = "www.google.com"

    text_node = TextNode(text, text_type, url)

    html_node = text_node_to_html_node(text_node)

    print(html_node)


main()
