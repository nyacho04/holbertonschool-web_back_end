#!/usr/bin/env python3
"""
calculate the runtime of wait_n.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ return time wiat_n takes"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    final = end - start_time
    return final / n
