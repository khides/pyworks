import asyncio

async def a():
    return True

async def main():
    if await a():
        print("a")
    
    
if __name__ == "__main__":
    asyncio.run(main())