from dataclasses import dataclass, field
from enum import Enum

class AsciiHierarchyEnvironmentStyle(Enum):
    """" Guides how the output is written to be used in different environments """

    TEXT_ENVIRONMENT_STYLE = "text_environment_style",
    MARKDOWN_ENVIRONMENT_STYLE = "markdown_environment_style",
    HTML_ENVIRONMENT_STYLE = "html_environment_style"

class AsciiHierarchyLayoutStyle(Enum):
    """" Gives the style of the layout for the hierarchy """

    MINIMAL_LAYOUT_STYLE = "minimal_layout_style",
    BOX_LAYOUT_STYLE = "box_layout_layout_style",
    ROUNDED_BOX_LAYOUT_STYLE = "rounded_box_layout_style",
    DOUBLE_LINE_LAYOUT_STYLE = "double_line_layout_style",
    PLUS_HYPHEN_LAYOUT_STYLE = "plus_hyphen_layout_style"

class AsciiHierarchyContextStyle(Enum):
    """" Adds more specific style based on the context of the hierarchy. For example, a folder hierarchy """

    MINIMAL_CONTEXT_STYLE = "minimal_context_style",
    FOLDER_CONTEXT_STYLE = "folder_context_style"

@dataclass
class AsciiHierarchyStyle:
    environment_style: AsciiHierarchyEnvironmentStyle = field(default_factory=AsciiHierarchyEnvironmentStyle)

    layout_style: AsciiHierarchyLayoutStyle = field(default_factory=AsciiHierarchyLayoutStyle)

    context_style: AsciiHierarchyContextStyle = field(default_factory=AsciiHierarchyContextStyle)