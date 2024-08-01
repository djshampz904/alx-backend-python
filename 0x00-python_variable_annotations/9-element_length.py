#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string k and an int OR float v as"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples, each containing an element and its length"""
    return [(i, len(i)) for i in lst]
