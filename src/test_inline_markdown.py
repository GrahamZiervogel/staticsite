import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import split_nodes_delimiter


class TestConversion(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT)])
        
    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("bold block", TextType.BOLD),
                                    TextNode(" word", TextType.TEXT)])
    
    def test_italic(self):
        node = TextNode("This is text with a *italic block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("italic block", TextType.ITALIC),
                                    TextNode(" word", TextType.TEXT)])
        
    def test_multi_bold(self):
        node = TextNode("This is text with a **bolded word** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD)],
                new_nodes)
        
    def test_bold_and_italic(self):
        node = TextNode("This is text with a **bolded part** and an *italic part*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded part", TextType.BOLD),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic part", TextType.ITALIC)],
                new_nodes)


if __name__ == "__main__":
    unittest.main()
