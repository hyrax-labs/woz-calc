"""Tests for the CLI surface in :mod:`cli`."""

import contextlib
import io
import unittest

import cli


def run_cli(argv):
    """Invoke ``cli.main`` in-process, returning (exit_code, stdout, stderr)."""
    stdout = io.StringIO()
    stderr = io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        exit_code = cli.main(argv)
    return exit_code, stdout.getvalue(), stderr.getvalue()


class SubcommandTests(unittest.TestCase):
    def test_add_prints_formatted_result(self):
        exit_code, stdout, stderr = run_cli(["add", "2", "3"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "5\n")
        self.assertEqual(stderr, "")

    def test_subtract_prints_formatted_result(self):
        exit_code, stdout, stderr = run_cli(["subtract", "5", "3"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "2\n")
        self.assertEqual(stderr, "")

    def test_multiply_prints_formatted_result(self):
        exit_code, stdout, stderr = run_cli(["multiply", "4", "3"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "12\n")
        self.assertEqual(stderr, "")

    def test_divide_prints_formatted_result(self):
        exit_code, stdout, stderr = run_cli(["divide", "7", "2"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "3.5\n")
        self.assertEqual(stderr, "")


class FormatResultTests(unittest.TestCase):
    def test_whole_float_renders_without_trailing_zero(self):
        self.assertEqual(cli.format_result(5.0), "5")

    def test_non_whole_float_renders_normally(self):
        self.assertEqual(cli.format_result(3.5), "3.5")

    def test_int_renders_normally(self):
        self.assertEqual(cli.format_result(5), "5")


class DivideByZeroTests(unittest.TestCase):
    def test_divide_by_zero_returns_one_and_writes_to_stderr_only(self):
        exit_code, stdout, stderr = run_cli(["divide", "1", "0"])
        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout, "")
        self.assertIn("divide by zero", stderr)


class ArgparseExitTests(unittest.TestCase):
    def test_non_numeric_operand_raises_system_exit_2(self):
        with self.assertRaises(SystemExit) as ctx:
            run_cli(["add", "x", "3"])
        self.assertEqual(ctx.exception.code, 2)

    def test_unknown_operation_raises_system_exit_2(self):
        with self.assertRaises(SystemExit) as ctx:
            run_cli(["foo", "1", "2"])
        self.assertEqual(ctx.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
