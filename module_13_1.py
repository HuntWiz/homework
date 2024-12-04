import asyncio

balls = 5


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, balls + 1):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Павел', 3))
    task2 = asyncio.create_task(start_strongman('Никита', 4))
    task3 = asyncio.create_task(start_strongman('Лев', 5))
    await task1, task2, task3



asyncio.run(start_tournament())
