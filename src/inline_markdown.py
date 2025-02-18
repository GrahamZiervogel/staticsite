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
