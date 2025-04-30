#!/usr/bin/env python3
"""notnote aaaaaaaaaaaaaaaaa"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """notnote aaaaaaaaaaaaaaaaa"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    fulltime = time.perf_counter()
    return fulltime - start_time
