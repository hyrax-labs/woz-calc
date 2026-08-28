"""Arithmetic operation functions extracted from calc.py."""


def add(a, b):
    if a is None or b is None:
        raise ValueError("inputs must not be None")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("inputs must be numbers")
    return a + b


def subtract(a, b):
    if a is None or b is None:
        raise ValueError("inputs must not be None")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("inputs must be numbers")
    return a - b


def multiply(a, b):
    if a is None or b is None:
        raise ValueError("inputs must not be None")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("inputs must be numbers")
    return a * b
