import asyncio

async def main():
    print("Working fine")
    task = asyncio.create_task(foo("Now"))
    await asyncio.sleep(0.5)
    print("Running tests")
    await task

async def foo(name):
    print("Running Foo")
    await asyncio.sleep(10)
    print(name)

asyncio.run(main())
