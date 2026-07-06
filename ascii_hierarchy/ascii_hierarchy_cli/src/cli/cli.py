import argparse
import sys
from core.parsers import Parser
from core.styles import AsciiHierarchyStylingUtils as styling
from core.styles import AsciiHierarchyStyle

def run():
    args = get_args()

    result = ""

    style = styling.get_style_from_stings(args.environment, args.layout, args.context)

    if args.one_line != "":
        result = Parser.parse_one_liner(args.one_line, style, args.debug)
    else:
        ...

    print(result)

def get_args():
    parser = argparse.ArgumentParser(description="CLI for creating ASCII hierarchy trees")

    parser.add_argument("-l","--one_line", type=str, default="", help="Create a tree from a one liner")
    parser.add_argument("-e", "--environment", type=str, default="text-env", help="Environment that the string result will go to")
    parser.add_argument("-f", "--layout", type=str, default="box", help="Layout of the hierarchy")
    parser.add_argument("-c", "--context", type=str, default="folder", help="Type of hierarchy context")
    parser.add_argument("-d", "--debug", type=bool, action="store_true", help="Turn on debug mode")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    run()