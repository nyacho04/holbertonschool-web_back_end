#!/usr/bin/env python3
"""
Module to add two float numbers.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        """multiply the input value by the multiplier."""
        return value * multiplier

    return multiply
