#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples, each containing"""
    return [(i, len(i)) for i in lst]
