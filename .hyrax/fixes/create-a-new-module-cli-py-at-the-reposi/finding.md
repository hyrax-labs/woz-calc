# Create a new module `cli.py` at the repository root that provides the CLI entry…

**Tool:** `task`
**Severity:** unspecified

## What's wrong

Create a new module `cli.py` at the repository root that provides the CLI entry point for woz-calc. It must use only the standard library (`argparse`, `sys`).

Requirements:
- Expose `build_parser()` returning a configured `argparse.ArgumentParser` with a program name of `woz-calc`, a short description, and one subcommand per arithmetic operation: `add`, `subtract`, `multiply`, `divide`. Each subcommand takes exactly two positional operands named `a` and `b`, parsed with `type=float`.
- Expose `main(argv=None)` which parses `argv` (defaulting to `sys.argv[1:]`), dispatches to the matching function imported from `calc`, prints the result to stdout, and returns `0`.
- Result formatting: print the numeric result on a single line. Format whole-number floats without a trailing `.0` (e.g. `2 + 3` prints `5`, `7 / 2` prints `3.5`). Implement this with a small helper such as `format_result(value)` so it can be unit tested directly.
- Guard execution with `if __name__ == "__main__": sys.exit(main())`.
- Invoking with no arguments must print help/usage and exit non-zero rather than crashing.
- Do NOT put argument parsing or printing into `calc.py`; `cli.py` imports from `calc`. Do NOT restructure `calc.py` into a class.

This step covers the happy path and argparse's own built-in usage errors; friendly handling of arithmetic errors (e.g. divide by zero) is the next step, so a `ZeroDivisionError` traceback escaping here is acceptable for now.
