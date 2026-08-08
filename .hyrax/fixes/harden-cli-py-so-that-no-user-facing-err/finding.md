# Harden `cli.py` so that no user-facing error surfaces as a raw Python traceback.

**Tool:** `task`
**Severity:** unspecified

## What's wrong

Harden `cli.py` so that no user-facing error surfaces as a raw Python traceback.

In `main(argv=None)`, wrap the dispatch/computation so that:
- `ZeroDivisionError` (raised by `calc.divide`) is caught and reported as a single clear line on **stderr**, prefixed consistently (e.g. `woz-calc: error: cannot divide by zero`), with `main()` returning `1`.
- Any other `ArithmeticError`/`OverflowError` from the arithmetic layer is likewise reported on stderr with a readable message and return code `1`.
- Non-numeric operands (e.g. `python cli.py add 2 abc`) are rejected by argparse with its standard usage error on stderr and exit code `2` — keep relying on `type=float` for this rather than hand-rolling validation, and confirm the message names the offending value.
- An unknown operation (e.g. `python cli.py modulo 1 2`) produces an argparse invalid-choice usage error on stderr and exit code `2`.
- The `if __name__ == "__main__"` guard passes `main()`'s return value to `sys.exit()` so exit codes propagate.

Do not swallow programmer errors: do not add a blanket `except Exception`. Keep the error-message strings simple and stable, since the next step asserts on them in tests. `calc.py` must not change in this step — error *raising* stays in `calc.py`, error *reporting* lives in `cli.py`.
