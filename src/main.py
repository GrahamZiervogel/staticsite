from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images

def main():
    text = """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and 
                ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"""
    print(extract_markdown_images(text))


main()
