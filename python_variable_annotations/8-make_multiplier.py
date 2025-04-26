#!/usr/bin/env python3
"""
Module to add two float numbers.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Typed function that takes a float number as an argument and returns a function."""
    def multiply(value: float) -> float:
        """Multiply the input value by the multiplier."""
        return value * multiplier

    return multiply
