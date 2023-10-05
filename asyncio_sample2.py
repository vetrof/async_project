import asyncio

async def foo():
    print("Запуск функции foo")
    await asyncio.sleep(2)
    print("Функция foo завершилась")

async def bar():
    print("Запуск функции bar")
    await asyncio.sleep(1)
    print("Функция bar завершилась")


loop = asyncio.get_event_loop()
tasks = [foo(), bar()]
loop.run_until_complete(asyncio.gather(*tasks))