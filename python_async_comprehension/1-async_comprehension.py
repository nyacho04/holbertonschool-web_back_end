#!/usr/bin/env python3
"""notnote aaaaaaaaaaaaaaaaa"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """note aaaaaaaaaaaaaaaaa"""
    value = [item async for item in async_generator()]
    return value
