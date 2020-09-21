'''
learn from: https://realpython.com/async-io-python/
'''

import asyncio
import random

# ANSI colors
c = (
        "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx})")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)

    print(c[idx + 1] + f"---> Finished: makerandom({idx})")
    return i

async def main():
    # https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean-in-a-function-call
    #res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    res = await asyncio.gather(*(makerandom(0, 9), makerandom(1, 9),
        makerandom(2, 9)))
    
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

