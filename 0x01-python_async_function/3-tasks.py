#!/usr/bin/env python3
"""Tasks"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task wait random"""
    return asyncio.create_task(wait_random(max_delay))
