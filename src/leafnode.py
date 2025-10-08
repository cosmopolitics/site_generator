from typing import override
from src.htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(
        self, tag: str | None, value: str | None, props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, props=props)

    @override
    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("all LeafNodes must have a value")

        if self.tag == None:
            return self.value

        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
