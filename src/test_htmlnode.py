import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = HTMLNode("a")
        node2 = HTMLNode("b")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("tag", "value", "children", "props")
        self.assertEqual(repr(node), "HTMLNode(tag, value, children, props)")

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()
