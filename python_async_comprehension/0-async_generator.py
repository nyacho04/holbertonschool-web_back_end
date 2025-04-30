#!/usr/bin/env python3
"""notedddddddddddd"""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """notedddddddddddddddddd"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
