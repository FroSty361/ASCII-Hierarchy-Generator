from ascii_hierarchy.structures import AsciiHierarchy, AsciiHierarchyNode


def main():
    test_node_is_in_hierarchy()

def test_node_is_in_hierarchy():
    ascii_hierarchy = AsciiHierarchy(name="test", root_node_name="test_root_name", style=None, debug_mode=True)
    root_child_one = AsciiHierarchyNode(name="root_child_one", hierarchy=ascii_hierarchy, parent_node=ascii_hierarchy.root_node)
    ascii_hierarchy.root_node.add_node(root_child_one)
    root_child_one_child = AsciiHierarchyNode(name="root_child_one_child", hierarchy=ascii_hierarchy, parent_node=root_child_one)
    root_child_one.add_node(root_child_one_child)

    assert ascii_hierarchy.node_is_in_hierarchy(root_child_one_child) == True


if __name__ == "__main__":
    main()