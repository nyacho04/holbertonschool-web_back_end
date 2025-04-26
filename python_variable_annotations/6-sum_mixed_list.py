#!/usr/bin/env python3
"""
takes a list mxd_lst of integers and floats and returns their sum
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of a list of floats"""
    return sum(mxd_lst)
