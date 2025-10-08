import unittest
from src.leafnode import LeafNode


class test_leafnodes(unittest.TestCase):
    def test_leafnode_tohtml_p(self):
        node = LeafNode("p", "Hello, world!").to_html()
        self.assertEqual(node, "<p>Hello, world!</p>")

    def test_leafnode_tohtml_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_tohtml_script(self):
        node = LeafNode("script", "a = 1; b=2; console.log(a+b);").to_html()
        self.assertEqual(node, "<script>a = 1; b=2; console.log(a+b);</script>")
