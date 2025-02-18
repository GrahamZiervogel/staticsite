import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node ", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.yahoo.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("test text", TextType.ITALIC, "google.com")
        self.assertEqual(repr(node), "TextNode(test text, italic, google.com)")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("text", TextType.TEXT)
        html_node = HTMLNode(None, "text", None, None)
        self.assertEqual(text_node_to_html_node(text_node), html_node)

    def test_bold(self):
        text_node = TextNode("text", TextType.BOLD)
        html_node = HTMLNode("b", "text", None, None)
        self.assertEqual(text_node_to_html_node(text_node), html_node)

    def test_italic(self):
        text_node = TextNode("text", TextType.ITALIC)
        html_node = HTMLNode("i", "text", None, None)
        self.assertEqual(text_node_to_html_node(text_node), html_node)

    def test_code(self):
        text_node = TextNode("text", TextType.CODE)
        html_node = HTMLNode("code", "text", None, None)
        self.assertEqual(text_node_to_html_node(text_node), html_node)

    def test_link(self):
        text_node = TextNode("text", TextType.LINK, "www.google.com")
        html_node = HTMLNode("a", "text", None, {"href": "www.google.com"})
        self.assertEqual(text_node_to_html_node(text_node), html_node)

    def test_image(self):
        text_node = TextNode("text", TextType.IMAGE, "www.image.com")
        html_node = HTMLNode("img", "", None, {"src": "www.image.com", "alt": "text"})
        self.assertEqual(text_node_to_html_node(text_node), html_node)


if __name__ == "__main__":
    unittest.main()
