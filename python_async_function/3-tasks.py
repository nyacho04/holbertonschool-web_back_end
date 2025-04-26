#!/usr/bin/env python3
"""
returns an asyncio task
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create and return an asynciotask for wait random"""
    return asyncio.create_task(wait_random(max_delay))
