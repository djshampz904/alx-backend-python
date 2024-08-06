#!/usr/bin/env python3
"""Concurrent coroutines"""

import asyncio
from typing import List, Any

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[Any]:
    """Wait and return the delay"""
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
