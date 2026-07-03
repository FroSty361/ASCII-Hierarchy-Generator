from ascii_hierarchy.ascii_hierarchy_core.src.core.structures import AsciiHierarchy, AsciiHierarchyNode
from ascii_hierarchy.ascii_hierarchy_core.src.core.styles import AsciiHierarchyEnvironmentStyle, AsciiHierarchyLayoutStyle, AsciiHierarchyContextStyle
from ascii_hierarchy.ascii_hierarchy_core.src.core.styles import AsciiHierarchyStyle

def main():
    test_node_is_in_hierarchy()
    test_show_hierarchy()

def test_node_is_in_hierarchy():
    ascii_hierarchy = AsciiHierarchy(name="test", root_node_name="test_root_name", style=None, debug_mode=True)
    root_child_one = AsciiHierarchyNode(name="root_child_one", hierarchy=ascii_hierarchy, parent_node=ascii_hierarchy.root_node)
    ascii_hierarchy.root_node.add_node(root_child_one)
    root_child_one_child = AsciiHierarchyNode(name="root_child_one_child", hierarchy=ascii_hierarchy, parent_node=root_child_one)
    root_child_one.add_node(root_child_one_child)

    assert ascii_hierarchy.node_is_in_hierarchy(root_child_one_child) == True

def test_show_hierarchy():
    style = AsciiHierarchyStyle(environment_style=AsciiHierarchyEnvironmentStyle.TEXT_ENVIRONMENT_STYLE, layout_style=AsciiHierarchyLayoutStyle.PLUS_HYPHEN_LAYOUT_STYLE, context_style=AsciiHierarchyContextStyle.FOLDER_CONTEXT_STYLE)

    ascii_hierarchy = AsciiHierarchy(name="test", root_node_name="test_root_name", style=style, debug_mode=True)
    root_child_one = AsciiHierarchyNode(name="root_child_one", hierarchy=ascii_hierarchy, parent_node=ascii_hierarchy.root_node)
    root_child_two = AsciiHierarchyNode(name="root_child_two", hierarchy=ascii_hierarchy, parent_node=ascii_hierarchy.root_node)
    ascii_hierarchy.root_node.add_node(root_child_one)
    ascii_hierarchy.root_node.add_node(root_child_two)
    root_child_one_child_one = AsciiHierarchyNode(name="root_child_one_child_one", hierarchy=ascii_hierarchy, parent_node=root_child_one)
    root_child_one_child_two = AsciiHierarchyNode(name="root_child_one_child_two", hierarchy=ascii_hierarchy, parent_node=root_child_one)
    root_child_one.add_node(root_child_one_child_one)
    root_child_one.add_node(root_child_one_child_two)
    root_child_one_child_two_child = AsciiHierarchyNode(name="root_child_one_child_two_child", hierarchy=ascii_hierarchy, parent_node=root_child_one_child_two)
    root_child_one_child_two.add_node(root_child_one_child_two_child)

    print(ascii_hierarchy.get_ascii_hierarchy())

    assert "purpose_fail_for_print" == ""

if __name__ == "__main__":
    main()