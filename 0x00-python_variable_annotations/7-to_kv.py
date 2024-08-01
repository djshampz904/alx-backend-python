#!/usr/bin/env python3
"""Type-annotated function to_kv that ts"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing k and the square of v"""
    return k, v * v
