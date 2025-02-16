import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("tag", "value")
        node2 = LeafNode("tag", "value")
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = LeafNode("tag1", "value1")
        node2 = LeafNode("tag2", "value2")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = LeafNode("tag", "value", "props")
        self.assertEqual(repr(node), "HTMLNode(tag, value, None, props)")

    def test_to_html_no_props(self):
        tag = "p"
        value = "This is a paragraph of text."
        node = LeafNode(tag, value)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_to_html_with_props(self):
        tag = "a"
        value = "Click me!"
        props = {"href": "https://www.google.com"}
        node = LeafNode(tag, value, props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()
