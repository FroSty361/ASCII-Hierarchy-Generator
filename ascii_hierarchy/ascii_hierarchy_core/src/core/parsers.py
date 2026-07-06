import sys
from core.structures import AsciiHierarchy
from core.styles import AsciiHierarchyStyle

class Parser:
    @staticmethod
    def parse_one_liner(one_liner: str, style: AsciiHierarchyStyle, debug_mode: bool = False) -> str:
        if len(one_liner) == 0:
            sys.exit("One Liner Syntax Error - There is no one liner")

        if not one_liner.endswith("]]"):
            sys.exit("One Liner Syntax Error - Expression must end with at least two closing square brackets")

        if one_liner.count("[") != one_liner.count("]"):
            sys.exit("One Liner Syntax Error - Amount of open square brackets must equal the amount of closing square brackets")

        one_liner = one_liner.replace(" ", "")

        hierarchy_name, first_bracket_index = Parser._one_liner_get_name(one_liner=one_liner, debug_mode=debug_mode, for_hierarchy_title=True)
        one_liner = one_liner[first_bracket_index:len(one_liner) - 1]
        root_node_name, next_bracket_index = Parser._one_liner_get_name(one_liner=one_liner, debug_mode=debug_mode, for_hierarchy_title=False)

        result = ""

        ascii_hierarchy = AsciiHierarchy(name=hierarchy_name, root_node_name=root_node_name, style=style, debug_mode=debug_mode)

        return result

    @staticmethod
    def one_liner_parse_children(one_liner: str, ascii_hierarchy: AsciiHierarchy, debug_mode: bool = False):
        ...

    @staticmethod
    def _one_liner_get_name(one_liner: str, debug_mode: bool = False, for_hierarchy_title: bool = False):
        bracket_index = one_liner.find("[")

        if bracket_index == -1:
            message = "One Liner Syntax Error - There must be an open square bracket after a name"

            if debug_mode:
                sys.exit(f'{message}.\nDepth in to expression is {one_liner}')
            else:
                sys.exit(message)
        elif bracket_index == 0:
            message = "One Liner Syntax Error - Names must come before an open square bracket"

            if debug_mode:
                sys.exit(f"{message}.\nDepth in to expression is {one_liner}")
            else:
                sys.exit(message)

        name = one_liner[:bracket_index]

        is_valid_name, invalid_character = Parser._check_if_valid_name(name=name)

        if not is_valid_name():
            if for_hierarchy_title:
                sys.exit(f"One Liner Name Error - Hierarchy name {one_liner} can not have {invalid_character}")
            else:
                sys.exit(f"One Liner Name Error - Name {one_liner} can not have {invalid_character}")

        return name, bracket_index

    @staticmethod
    def _check_if_valid_name(name: str):
        invalid_characters = [" ", "[", "]", "/", "\\", ":", "*", "?", "\"", "<", ">", "|"]

        for invalid_character in invalid_characters:
            if invalid_character in name:
                return False, invalid_character

        return True, ""