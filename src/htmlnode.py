from typing import override


class HtmlNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HtmlNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HtmlNode] | None = children
        self.props: dict[str, str] | None = props

    @override
    def __repr__(self) -> str:
        string = f"HtmlNode({self.tag}, {self.value}"
        if self.children != None:
            for child in self.children:
                string += f", {child.__repr__()}"
        else:
            string += ", None"

        string += f", {self.props})"
        return string

    def props_to_html(self) -> str:
        props_string = ""
        if self.props == None:
            return " None"
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'

        return props_string

    def to_html(self) -> str:
        raise NotImplementedError
