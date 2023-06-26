import asyncio

async def func(x):
    return x*2

async def run():
    x = await func(1)
    print(x)

if __name__ == "__main__":
    asyncio.run(run())