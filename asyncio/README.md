# Learn asyncio

Source:

- next: https://realpython.com/async-io-python/#async-io-in-context

Some concepts/terms to grab first:

### Coroutine

A **coroutine** is a function that can suspend its execution in the middle, and indirectly let the other coroutine to run for some time, before it continues its operation.

How to make a coroutine with the keyword `async`:

```python
async def my_coroutine():
    pass
```

To call a coroutine funcntion, we must `await` to get the results.

### The `await` keyword

The keyword `await` tells: "just wait for me until this line returns. In the meantime, you can do something else"

```python
async def my_coroutine():
    # pause here and let the other coroutine do something else
    # come back here when f() finishes
    result = await f()
    return result
```

We can only use `await` inside the body of a coroutine. For example, we cannot do this:

```python
# this is NOT going to work (SyntaxError):
def func():
    res = await f()
    return res
```

The `await`ed functions must be awaitable: they are also coroutines. That being said, in the example above, the `f()` is a coroutine (`async def f(): ...`).

### Event loop

Event loop is like a `while True` that monitors the coroutines, looks at what's idle, and do look on something else to do in the meantime.

The management of the event loop is handled by the function call `asyncio.run()`:

```python
asyncio.run(main())
```

Coroutines have to be tied to the event loop: call the coroutines with `asyncio.run(coroutine())`.

A faster implementations of event loop is [uvloop](https://github.com/MagicStack/uvloop).

