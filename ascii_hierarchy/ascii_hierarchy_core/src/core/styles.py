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

class AsciiHierarchyStylingUtils:

    # Ascii Hierarchy Environment

    @staticmethod
    def get_environment_start(text: str, environment_style: AsciiHierarchyEnvironmentStyle | None):
        match environment_style:
            case AsciiHierarchyEnvironmentStyle.TEXT_ENVIRONMENT_STYLE:
                return f"{text}\n\n"
            case AsciiHierarchyEnvironmentStyle.MARKDOWN_ENVIRONMENT_STYLE:
                return f"# {text}\n\n```"
            case AsciiHierarchyEnvironmentStyle.HTML_ENVIRONMENT_STYLE:
                return f"<h1>{text}</h1>\n\n"
            case _:
                return f"{text}\n\n"

    @staticmethod
    def get_environment_end(text: str, environment_style: AsciiHierarchyEnvironmentStyle | None):
        match environment_style:
            case AsciiHierarchyEnvironmentStyle.TEXT_ENVIRONMENT_STYLE:
                return ""
            case AsciiHierarchyEnvironmentStyle.MARKDOWN_ENVIRONMENT_STYLE:
                return "```"
            case AsciiHierarchyEnvironmentStyle.HTML_ENVIRONMENT_STYLE:
                return ""
            case _:
                return ""

    @staticmethod
    def get_environment_line(text: str, environment_style: AsciiHierarchyEnvironmentStyle | None):
        match environment_style:
            case AsciiHierarchyEnvironmentStyle.TEXT_ENVIRONMENT_STYLE:
                return text
            case AsciiHierarchyEnvironmentStyle.MARKDOWN_ENVIRONMENT_STYLE:
                return text
            case AsciiHierarchyEnvironmentStyle.HTML_ENVIRONMENT_STYLE:
                return f"<p>{text}</p>"
            case _:
                return text

    # Ascii Hierarchy Layout

    @staticmethod
    def get_layout_style_horizontal(layout_style: AsciiHierarchyLayoutStyle | None):
        match layout_style:
            case AsciiHierarchyLayoutStyle.MINIMAL_LAYOUT_STYLE:
                return ""
            case AsciiHierarchyLayoutStyle.BOX_LAYOUT_STYLE:
                return "─"
            case AsciiHierarchyLayoutStyle.ROUNDED_BOX_LAYOUT_STYLE:
                return "─"
            case AsciiHierarchyLayoutStyle.DOUBLE_LINE_LAYOUT_STYLE:
                return "═"
            case AsciiHierarchyLayoutStyle.PLUS_HYPHEN_LAYOUT_STYLE:
                return "-"
            case _:
                return ""

    @staticmethod
    def get_layout_style_vertical(layout_style: AsciiHierarchyLayoutStyle | None):
        match layout_style:
            case AsciiHierarchyLayoutStyle.MINIMAL_LAYOUT_STYLE:
                return ""
            case AsciiHierarchyLayoutStyle.BOX_LAYOUT_STYLE:
                return "│"
            case AsciiHierarchyLayoutStyle.ROUNDED_BOX_LAYOUT_STYLE:
                return "│"
            case AsciiHierarchyLayoutStyle.DOUBLE_LINE_LAYOUT_STYLE:
                return "║"
            case AsciiHierarchyLayoutStyle.PLUS_HYPHEN_LAYOUT_STYLE:
                return "|"
            case _:
                return ""

    @staticmethod
    def get_layout_style_top_corner(layout_style: AsciiHierarchyLayoutStyle | None):
        match layout_style:
            case AsciiHierarchyLayoutStyle.MINIMAL_LAYOUT_STYLE:
                return ""
            case AsciiHierarchyLayoutStyle.BOX_LAYOUT_STYLE:
                return "┌"
            case AsciiHierarchyLayoutStyle.ROUNDED_BOX_LAYOUT_STYLE:
                return "╭"
            case AsciiHierarchyLayoutStyle.DOUBLE_LINE_LAYOUT_STYLE:
                return "╔"
            case AsciiHierarchyLayoutStyle.PLUS_HYPHEN_LAYOUT_STYLE:
                return "+"
            case _:
                return ""

    @staticmethod
    def get_layout_style_bottom_corner(layout_style: AsciiHierarchyLayoutStyle | None):
        match layout_style:
            case AsciiHierarchyLayoutStyle.MINIMAL_LAYOUT_STYLE:
                return ""
            case AsciiHierarchyLayoutStyle.BOX_LAYOUT_STYLE:
                return "└"
            case AsciiHierarchyLayoutStyle.ROUNDED_BOX_LAYOUT_STYLE:
                return "╰"
            case AsciiHierarchyLayoutStyle.DOUBLE_LINE_LAYOUT_STYLE:
                return "╚"
            case AsciiHierarchyLayoutStyle.PLUS_HYPHEN_LAYOUT_STYLE:
                return "+"
            case _:
                return ""

    @staticmethod
    def get_layout_style_intersection(layout_style: AsciiHierarchyLayoutStyle | None):
        match layout_style:
            case AsciiHierarchyLayoutStyle.MINIMAL_LAYOUT_STYLE:
                return ""
            case AsciiHierarchyLayoutStyle.BOX_LAYOUT_STYLE:
                return "├"
            case AsciiHierarchyLayoutStyle.ROUNDED_BOX_LAYOUT_STYLE:
                return "├"
            case AsciiHierarchyLayoutStyle.DOUBLE_LINE_LAYOUT_STYLE:
                return "╠"
            case AsciiHierarchyLayoutStyle.PLUS_HYPHEN_LAYOUT_STYLE:
                return "+"
            case _:
                return ""

    # Ascii Hierarchy Context

    @staticmethod
    def get_context_name_ending(context_style: AsciiHierarchyContextStyle | None):
        match context_style:
            case AsciiHierarchyContextStyle.MINIMAL_CONTEXT_STYLE:
                return ""
            case AsciiHierarchyContextStyle.FOLDER_CONTEXT_STYLE:
                return "/"
            case _:
                return ""

    # Hierarchy Styling

    @staticmethod
    def get_node_line(node_name: str, style: AsciiHierarchyStyle, is_last: bool, parent_child_amount: int) -> str:
        result = ""

        pipe = AsciiHierarchyStylingUtils.get_layout_style_horizontal(style.layout_style)
        context_name_ending = AsciiHierarchyStylingUtils.get_context_name_ending(style.context_style)
        layout_start = AsciiHierarchyStylingUtils.get_layout_style_intersection(style.layout_style)

        if is_last:
            layout_start = AsciiHierarchyStylingUtils.get_layout_style_bottom_corner(style.layout_style)

        result += f"{layout_start}{pipe}{pipe}{node_name}{context_name_ending}\n"

        return result