from src.textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
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
            elif split_text[i] != '':
                new_nodes.append(TextNode(split_text[i], TextType.text, None))

    return new_nodes
