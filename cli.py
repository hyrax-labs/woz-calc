"""Command-line entry point for woz-calc.

This module owns all argument parsing, dispatch, and output formatting.
The arithmetic itself lives in :mod:`calc`; this module simply wires a
stdlib ``argparse`` interface to those functions.
"""

import argparse
import sys

from calc import add, divide, multiply, subtract

_OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def build_parser():
    """Build and return the ``woz-calc`` argument parser."""
    parser = argparse.ArgumentParser(
        prog="woz-calc",
        description="A tiny command-line calculator.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name in _OPERATIONS:
        subparser = subparsers.add_parser(name, help=f"{name} two numbers")
        subparser.add_argument("a", type=float, help="first operand")
        subparser.add_argument("b", type=float, help="second operand")

    return parser


def format_result(value):
    """Format a numeric result for display.

    Whole-number floats are printed without a trailing ``.0``
    (e.g. ``5`` instead of ``5.0``), while non-integral values keep
    their normal ``str()`` representation (e.g. ``3.5``).
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main(argv=None):
    """Parse ``argv``, dispatch to the matching ``calc`` function, and print the result."""
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()
    args = parser.parse_args(argv)

    operation = _OPERATIONS[args.command]
    result = operation(args.a, args.b)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
