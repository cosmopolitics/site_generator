def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    cleaned_blocks: list[str] = []
    for block in blocks:
        cleaned_blocks.append(block.strip())

    return cleaned_blocks
