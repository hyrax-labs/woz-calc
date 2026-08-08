# Add a `divide(a, b)` function to `calc.py`, following the existing conventions…

**Tool:** `task`
**Severity:** unspecified

## What's wrong

Add a `divide(a, b)` function to `calc.py`, following the existing conventions exactly: a standalone top-level function taking exactly two positional operands, in the same style as `add`, `subtract`, and `multiply`. Do NOT introduce a class, a dispatch table, or any third-party import.

`divide(a, b)` must return `a / b` (true division) for a non-zero `b`. When `b == 0`, it must raise `ZeroDivisionError` with a clear human-readable message such as "cannot divide by zero" rather than letting the bare interpreter error surface — i.e. explicitly check for the zero divisor and `raise ZeroDivisionError("cannot divide by zero")`.

Do not modify the behaviour or signatures of `add`, `subtract`, or `multiply`. Keep `calc.py` free of I/O, printing, and argument parsing — it stays a pure arithmetic module. If the existing functions have docstrings, give `divide` one in the same style; if they do not, do not add one (match the file's existing style).
