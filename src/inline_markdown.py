import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type == TextType.TEXT) and (delimiter in node.text): 
            text_parts = node.text.split(delimiter)
            split_nodes = []
            if (len(text_parts) % 2) == 0:
                raise Exception("Invalid Markdown syntax: no closing delimiter found")
            for part_index in range(len(text_parts)):
                if text_parts[part_index] == "":
                    continue
                if part_index % 2 == 0:
                    split_nodes.append(TextNode(text_parts[part_index], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(text_parts[part_index], text_type))
            new_nodes.extend(split_nodes)
        else:
            new_nodes.append(node)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            link_text = link[0]
            link_url = link[1]

            sections = text.split(f"[{link_text}]({link_url})", 1)

            if len(sections) != 2:
                raise ValueError("Markdown error: link section is not closed")

            if sections[0] != "":
                textNode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textNode)

            linkNode = TextNode(link_text, TextType.LINK, link_url)
            new_nodes.append(linkNode)

            text = sections[1]

        if text != "":
            textNode = TextNode(text, TextType.TEXT)
            new_nodes.append(textNode)

        return new_nodes    

            
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue

        text = node.text
        imgs = extract_markdown_images(text)

        if len(imgs) == 0:
            new_nodes.append(node)
            continue

        for img in imgs:
            img_text = img[0]
            img_url = img[1]

            sections = text.split(f"![{img_text}]({img_url})", 1)

            if len(sections) != 2:
                raise ValueError("Markdown error: img section is not closed")

            if sections[0] != "":
                textNode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textNode)

            imgNode = TextNode(img_text, TextType.IMAGE, img_url)
            new_nodes.append(imgNode)

            text = sections[1]

        if text != "":
            textNode = TextNode(text, TextType.TEXT)
            new_nodes.append(textNode)

        return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "*", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
