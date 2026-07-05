import argparse
import sys
from core.parsers import Parser
from core.styles import AsciiHierarchyStylingUtils as styling
from core.styles import AsciiHierarchyStyle

def run():
    args = get_args()

    if args.one_line == "":
        sys.exit("-l / --one_line argument must be specified")

    style = styling.get_style_from_stings(args.environment, args.layout, args.context)

    result = Parser.parse_one_liner(args.one_line)

def get_args():
    parser = argparse.ArgumentParser(description="CLI for creating ASCII hierarchy trees")

    parser.add_argument("-l","--one_line", type=str, default="", help="Create a tree from a one liner")
    parser.add_argument("-e", "--environment", type=str, default="text-env", help="Environment that the string result will go to")
    parser.add_argument("-f", "--layout", type=str, default="box", help="Layout of the hierarchy")
    parser.add_argument("-c", "--context", type=str, default="folder", help="Type of hierarchy context")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    run()