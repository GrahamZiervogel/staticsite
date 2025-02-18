from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter

def main():
    node = TextNode("This is text with a **bolded word** and **another**", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    print(new_nodes)


main()
