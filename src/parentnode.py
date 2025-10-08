from typing import override
from src.htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(
        self,
        tag: str | None,
        children: list["HtmlNode"] | None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, children=children, props=props)

    @override
    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have a children")

        if self.props == None:
            html = f"<{self.tag}>"
        else:
            html = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html

    @override
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
