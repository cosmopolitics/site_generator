import unittest
from src.inline_markdown_parsing import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

from src.textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold),
                TextNode(" word and ", TextType.text),
                TextNode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded word", TextType.bold),
                TextNode(" and ", TextType.text),
                TextNode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("italic", TextType.italic),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.italic)
        self.assertListEqual(
            [
                TextNode("bold", TextType.bold),
                TextNode(" and ", TextType.text),
                TextNode("italic", TextType.italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link to imgur](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link to imgur", "https://i.imgur.com/zjjcJKZ.png")], matches)


if __name__ == "__main__":
    _ = unittest.main()
