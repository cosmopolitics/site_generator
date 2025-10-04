import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a link node", TextType.link, "https://google.com")
        node2 = TextNode("This is a link node", TextType.link, "https://google.com")
        self.assertEqual(node, node2)

    def test_repr2(self):
        node = TextNode("This is a link node", TextType.link)
        node2 = TextNode("This is a link node", TextType.link)
        self.assertEqual(node, node2)

    def test_repr3(self):
        node = TextNode("This is a link node", TextType.text)
        node2 = TextNode("This is a link node", TextType.link)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    _ = unittest.main()
