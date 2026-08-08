# Introduce the repository's first test infrastructure using only the standard li…

**Tool:** `task`
**Severity:** unspecified

## What's wrong

Introduce the repository's first test infrastructure using only the standard library `unittest` module. Do NOT add pytest or any other third-party test dependency, and do not add a dependency manifest.

Create:
- `tests/__init__.py` (may be empty) so `python -m unittest discover` works from the repository root with the root on `sys.path`.
- `tests/test_calc.py` covering the arithmetic layer: `add`, `subtract`, `multiply`, and `divide` for positive, negative, and zero operands; float results; and `divide(x, 0)` raising `ZeroDivisionError` (use `assertRaises` and assert the message mentions dividing by zero).
- `tests/test_cli.py` covering the CLI surface by calling `cli.main([...])` in-process (not by spawning subprocesses) and capturing stdout/stderr with `contextlib.redirect_stdout` / `redirect_stderr` or `unittest.mock.patch`:
  - each of the four subcommands returns `0` and prints the expected formatted result (`add 2 3` -> `5`, `divide 7 2` -> `3.5`);
  - `format_result` renders whole floats without `.0` and non-whole floats normally;
  - `divide 1 0` returns `1` and writes a divide-by-zero message to stderr with nothing on stdout;
  - a non-numeric operand and an unknown operation each raise `SystemExit` with code `2` (argparse exits directly — assert with `assertRaises(SystemExit)` and check `.code`).

Use plain `unittest.TestCase` classes and descriptive test method names. Every test must pass. Do not modify `calc.py` or `cli.py` in this step except to fix a genuine bug the tests expose — if you do, keep the change minimal and note it in the commit message.
