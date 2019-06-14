This notes were taken when learning from here:
- https://realpython.com/async-io-python/
- https://hackernoon.com/a-simple-introduction-to-pythons-asyncio-595d9c9ecf8c

# Basic Concepts
- Concurrency: imagine having 2 threads running on a single core CPU. Instructions from each thread could be interleaved, but only one of the two threads is actively running at a time.
- Parallelism: imagine having two threads running on different cores of a multi-core CPU.
- Asynchronous: a higher level programming concept -- when running a task, decide while the result of that task is not out yet, we'd do other work instead while waiting.

```
Parallelism implies concurrency 
(remember p -> q rule)
```

- CPU-bound tasks: tasks that is characterized by the computer's cores continually working hard
- IO-bound tasks: tasks that is characterized by a lot of waiting on i/o operation to complete.

# async IO
- async IO is a style of concurrent programming (not paralellism, see above notes)
- it is not threading, not multiprocessing
- it gives a feeling of concurrency despite using a single thread in a single process

## The rules of async IO
To create coroutine:
```python
async def function_name():
    pass
```

`await` must be used to call coroutine.

Summary of the rules:
```python
async def f(x):
    y = await z(x) # OK
    return y

def m(x):
    y = await z(x) # NO
    return y
```