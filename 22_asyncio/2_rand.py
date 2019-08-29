"""
Example taken from here:
https://realpython.com/async-io-python/

a corouting makerandom() keeps producing random int
in the range (0, 10). Until one of them exceeds a threshold,
let multiple calls of this corouting not need to wait
for each other to complete in succession.
"""

import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def randint(a: int, b: int) -> int:
    return random.randint(a, b)

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = await randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = await randint(0, 10)
    
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    # gather tasks
    res = await asyncio.gather(
        *(makerandom(i, 10 - i -1) for i in range(3))
    )
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")