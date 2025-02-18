from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    tag = "p"
    children = [LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text", {"href": "https://www.yahoo.com"}),
        LeafNode(None, "Normal text")]
    props = {"href": "https://www.google.com"}

    node = ParentNode(tag, children, props)

    print(node)
    print(node.to_html())


main()
