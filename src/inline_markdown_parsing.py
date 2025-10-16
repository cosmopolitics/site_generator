import re
from src.textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type is not TextType.text:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("closing delimiter not found")

        for i in range(0, len(split_text)):
            if i % 2 == 1:
                new_nodes.append(TextNode(split_text[i], text_type, None))
            elif split_text[i] != "":
                new_nodes.append(TextNode(split_text[i], TextType.text, None))

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(sections) != 2:
                raise ValueError("Invalid Markdown, Image not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.text))

            new_nodes.append(TextNode(image_alt, TextType.image, image_link))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.text))
    return new_nodes


def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in nodes:
        if old_node.text_type != TextType.text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.text))
            new_nodes.append(TextNode(link[0], TextType.link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.text))
    return new_nodes


def text_to_textnodes(text: str):
    nodes = [TextNode(text, TextType.text)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "_", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
