#!/usr/bin/env python3
"""
    Import async_comprehension from the previous file and write
    measure_runtime coroutine that will execute
    async_comprehension four times in parallel using
    asyncio.gather.
    measure_runtime should measure the total runtime and
    return it.
"""
import time
import asyncio
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime function"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
