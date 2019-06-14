"""
Example taken from here:
https://realpython.com/async-io-python/
"""
import asyncio

# definition of coroutine
async def count():
    print("one")
    """
    when it reaches "await", the function gives control
    to event loop and event loop will do another task
    until this "await" finishes
    """
    await asyncio.sleep(1)
    print("two")

async def main():
    await asyncio.gather(count(), count(), count()) # gather tasks

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main()) # event loop
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed: 0.2f} seconds")
