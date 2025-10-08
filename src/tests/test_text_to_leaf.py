from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from src.text_to_leaf import textnode_to_leafnode
import unittest


class test_text_to_leaf(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.text)
        html_node: LeafNode = textnode_to_leafnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.image, "https://www.boot.dev")
        html_node = textnode_to_leafnode(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.bold)
        html_node = textnode_to_leafnode(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    _ = unittest.main()
