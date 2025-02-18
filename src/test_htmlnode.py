import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = HTMLNode("tag", "value", [LeafNode("a", "a")], {"href": "www.google.com"})
        self.assertEqual(repr(node),
            "HTMLNode(tag, value, children: [LeafNode(a, a, None)], {'href': 'www.google.com'})")

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


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
        node = LeafNode("tag", "value", {"href": "www.google.com"})
        self.assertEqual(repr(node), "LeafNode(tag, value, {'href': 'www.google.com'})")

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


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("tag", [LeafNode("a", "a")])
        node2 = ParentNode("tag", [LeafNode("a", "a")])
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = ParentNode("tag1", [LeafNode("a", "a")])
        node2 = ParentNode("tag2", [LeafNode("b", "b")])
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = ParentNode("tag", [LeafNode("a", "a")], {"href": "www.google.com"})
        self.assertEqual(repr(node), 
            "ParentNode(tag, children: [LeafNode(a, a, None)], {'href': 'www.google.com'})")

    def test_to_html_no_props(self):
        tag = "p"
        children = [LeafNode("b", "Bold text")]
        node = ParentNode(tag, children)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")
    
    def test_to_html_with_props(self):
        tag = "a"
        children = [LeafNode("b", "Bold text")]
        props = {"href": "https://www.google.com"}
        node = ParentNode(tag, children, props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com"><b>Bold text</b></a>')

    def test_nested_parents(self):
        tag = "a"
        children = [ParentNode("x", [LeafNode("b", "bold text")]), LeafNode("c", "curve text")]
        props = {"href": "https://www.google.com"}
        node = ParentNode(tag, children, props)
        self.assertEqual(node.to_html(),
            '<a href="https://www.google.com"><x><b>bold text</b></x><c>curve text</c></a>')
    
    def test_nested_parents_with_props(self):
        tag = "a"
        children = [ParentNode("x", [LeafNode("b", "bold text")], {"cref": "cheese"}),
                    LeafNode("d", "dimple", {"eref": "energy", "fref": "fish"})]
        props = {"href": "https://www.google.com"}
        node = ParentNode(tag, children, props)
        self.assertEqual(node.to_html(),
            '<a href="https://www.google.com"><x cref="cheese"><b>bold text</b></x>' +
            '<d eref="energy" fref="fish">dimple</d></a>')
    

if __name__ == "__main__":
    unittest.main()
