from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return (self.text == text_node.text and
             self.text_type == text_node.text_type and
             self.url == text_node.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        tag = None
        value = text_node.text
        html_node = LeafNode(tag, value)
    elif text_node.text_type == TextType.BOLD:
        tag = "b"
        value = text_node.text
        html_node = LeafNode(tag, value)
    elif text_node.text_type == TextType.ITALIC:
        tag = "i"
        value = text_node.text
        html_node = LeafNode(tag, value)
    elif text_node.text_type == TextType.CODE:
        tag = "code"
        value = text_node.text
        html_node = LeafNode(tag, value)
    elif text_node.text_type == TextType.LINK:
        tag = "a"
        value = text_node.text
        props = {"href": text_node.url}
        html_node = LeafNode(tag, value, props)
    elif text_node.text_type == TextType.IMAGE:
        tag = "img"
        value = ""
        props = {"src": text_node.url, "alt": text_node.text}
        html_node = LeafNode(tag, value, props)
    else:
        raise Exception("Unknown text node type")
    
    return html_node
