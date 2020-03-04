import asyncio
import time


def now(): return time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    return f'Done after {x}s'


def callback(future):
    print('Callback: ', future.result())


if __name__ == '__main__':
    start = now()
    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    print(task)
    print(coroutine)

    task.add_done_callback(callback)

    loop.run_until_complete(task)
    print(loop)

    print('TIME: ', now() - start)

# import time
# import asyncio

# now = lambda : time.time()

# async def do_some_work(x):
#     print('Waiting: ', x)
#     return 'Done after {}s'.format(x)

# def callback(future):
#     print('Callback: ', future.result())

# start = now()

# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# loop.run_until_complete(task)

# print('TIME: ', now() - start)
