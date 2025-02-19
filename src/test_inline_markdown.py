import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT)])
        
    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("bold block", TextType.BOLD),
                                    TextNode(" word", TextType.TEXT)])
    
    def test_italic(self):
        node = TextNode("This is text with a *italic block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
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


class TestSplitNodesLink(unittest.TestCase):
    def test_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a link ", TextType.TEXT),
                              TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                              TextNode(" and ", TextType.TEXT),
                              TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")],
                              new_nodes)
    
    def test_more_links(self):
        node = TextNode("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT),
                              TextNode("link", TextType.LINK, "https://boot.dev"),
                              TextNode(" and ", TextType.TEXT),
                              TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                              TextNode(" with text that follows", TextType.TEXT)],
                              new_nodes)


class TestSplitNodesImage(unittest.TestCase):
    def test_split_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),
                              TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],
                              new_nodes)

    def test_split_image_single(self):
        node = TextNode("![image](https://www.example.COM/IMAGE.PNG)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG")],
                              new_nodes)

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),
                              TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                              TextNode(" and another ", TextType.TEXT),
                              TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")],
                              new_nodes)


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_images(self):
        text = """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and 
                ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"""
        md_images = extract_markdown_images(text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                              ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
                                md_images)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_links(self):
        text = """This is text with a link [to boot dev](https://www.boot.dev) and 
        [to youtube](https://www.youtube.com/@bootdotdev)"""
        md_links = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                              ("to youtube", "https://www.youtube.com/@bootdotdev")],
                                md_links)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = [TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")]
        self.assertListEqual(text_to_textnodes(text), nodes)


if __name__ == "__main__":
    unittest.main()
