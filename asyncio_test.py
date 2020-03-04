#%%
import time
import asyncio


async def hello():
    asyncio.sleep(1)
    print("Hello world: %s" % time.time())

def hello2():
    time.sleep(1)
    print("Hello world: %s" % time.time())

if __name__ == "__main__":
   loop = asyncio.get_event_loop()

   for i in range(5):
       loop.run_until_complete(hello())


#%%
import asyncio, time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "hello")
    await say_after(2, 'world')
    print(f'finished at {time.strftime("%X")}')

asyncio.run(main())


    


# %%
