import unittest
from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HtmlNode(
            None,
            "This is a link node",
            children=[HtmlNode("p", "this is a child node of a 'link node'")],
        )
        node2 = "HtmlNode(None, This is a link node, HtmlNode(p, this is a child node of a 'link node', None, None), None)"
        self.assertEqual(node.__repr__(), node2)

    def test_different_children(self):
        node = HtmlNode("div", children=[HtmlNode("p"), HtmlNode("a")])
        node2 = HtmlNode(
            "div", children=[HtmlNode("p", children=[HtmlNode("span")]), HtmlNode("a")]
        )
        self.assertNotEqual(node, node2)

    def test_to_html_props(self):
        node = HtmlNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HtmlNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr_two(self):
        node = HtmlNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HtmlNode(p, What a strange world, None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    _ = unittest.main()
