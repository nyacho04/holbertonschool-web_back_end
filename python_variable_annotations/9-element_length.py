#!/usr/bin/env python3
"""
variable
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of tuples."""
    return [(i, len(i)) for i in lst]
