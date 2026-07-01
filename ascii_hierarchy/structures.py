from .styles import AsciiHierarchyStyle, AsciiHierarchyEnvironmentStyle, AsciiHierarchyLayoutStyle, AsciiHierarchyContextStyle

class AsciiHierarchy:
    def __init__(self, name: str, root_node_name: str, style: AsciiHierarchyStyle | None, debug_mode: bool = False):
        self.name = name
        self.style = style

        self.debug_mode = debug_mode

        self._root_node = None
        self.root_node = AsciiHierarchyNode(name=root_node_name, hierarchy=self, parent_node=None)

    def __str__(self):
        if self.debug_mode:
            stats = self.get_stats()

            return stats
        else:
            ascii_hierarchy = self.get_ascii_hierarchy()

            return ascii_hierarchy

    def get_ascii_hierarchy(self) -> str:
        ascii_hierarchy = f"{self.name}\n\n"

        return ascii_hierarchy

    def get_stats(self) -> str:
        stats = f"{self.name}\n"

        stats += f"Root Node = {self.root_node.name}\n"

        return stats

    def node_is_in_hierarchy(self, node: AsciiHierarchyNode) -> bool:
        result = False

        result = self.root_node.has_node(node, False)

        return result

    # Properties

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def style(self) -> AsciiHierarchyStyle:
        return self._style

    @style.setter
    def style(self, style: AsciiHierarchyStyle | None):
        if style is None:
            print("AsciiHierarchyStyle can not be None. Setting style to default values")

            style = AsciiHierarchyStyle(environment_style=AsciiHierarchyEnvironmentStyle.TEXT_ENVIRONMENT_STYLE,
                                        layout_style=AsciiHierarchyLayoutStyle.MINIMAL_LAYOUT_STYLE,
                                        context_style=AsciiHierarchyContextStyle.MINIMAL_CONTEXT_STYLE)

        self._style = style

    @property
    def root_node(self) -> AsciiHierarchyNode:
        return self._root_node

    @root_node.setter
    def root_node(self, node: AsciiHierarchyNode):
        self._root_node = node

class AsciiHierarchyNode:
    def __init__(self, name: str, hierarchy: AsciiHierarchy, parent_node: AsciiHierarchyNode | None):
        self.name = name
        self._hierarchy = hierarchy

        if parent_node is not None:
            self._parent_node = parent_node
        else:
            if self._hierarchy.root_node is None: # Then this will be root node
                self._parent_node = parent_node
            else:
                raise TypeError(f"AsciiHierarchyNode parent node can not be None unless the node is root node")

        self._children: set[AsciiHierarchyNode] = set()

    def __str__(self):
        return self.name

    def add_node(self, node: AsciiHierarchyNode):
        if node == self:
            print(f"Can not add AsciiHierarchyNode aa a child to itself")

            return

        if node.hierarchy is not None and node.hierarchy != self._hierarchy:
            raise ValueError(f"Can not add AsciiHierarchyNode in Hierarchy {node.hierarchy.name} to node in hierarchy {self._hierarchy.name}")
        elif node.hierarchy == self._hierarchy:
            if self._hierarchy.node_is_in_hierarchy(node):
                if node.parent_node == self._hierarchy.root_node:
                    print(f"Can not add node AsciiHierarchyNode to {self._hierarchy.name} because it is already in the same hierarchy as root node")
                else:
                    print(f"Can not add node AsciiHierarchyNode to {self._hierarchy.name} because it is already in the same hierarchy with parent node {node.parent_node.name}")

                return

        self._children.add(node)

    def has_node(self, node: AsciiHierarchyNode, surface_level: bool) -> bool:
        if surface_level:
            return node in self._children
        else:
            for child_node in self._children:
                if child_node.has_node(node, False):
                    return True

        return False

    # Properties

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def hierarchy(self) -> AsciiHierarchy:
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy: AsciiHierarchy):
        self._hierarchy = hierarchy

    @property
    def parent_node(self) -> AsciiHierarchyNode | None:
        return self._parent_node

    @property
    def children(self) -> tuple[AsciiHierarchyNode, ...]:
        return tuple(self._children)