from src.textnode import TextNode, TextType
from src.leafnode import LeafNode


def textnode_to_leafnode(node: TextNode) -> LeafNode:
    match node.text_type:
        case TextType.text:
            return LeafNode(None, node.text)
        case TextType.bold:
            return LeafNode("b", node.text)
        case TextType.italic:
            return LeafNode("i", node.text)
        case TextType.code:
            return LeafNode("code", node.text)
        case TextType.link:
            if node.url is None:
                raise ValueError("textnode of type link doesnt contain a url")
            return LeafNode("a", node.text, {"href": node.url})
        case TextType.image:
            if node.url is None:
                raise ValueError("textnode of type image doesnt contain a url")
            return LeafNode("img", "", {"src": node.url, "alt": node.text})
