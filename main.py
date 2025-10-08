
def main():
    node = "**bold** and _italic_"
    node_two = "This is text with a **bolded** word and **another**"
    new_nodes = []
    new_nodes.append(node.split("**", 3))
    new_nodes.append(node.split("_", 3))
    new_nodes.append(node_two.split("**"))

    for nodes in new_nodes:
        print(nodes)

if __name__ == "__main__":
    main()
