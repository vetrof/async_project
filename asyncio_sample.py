import asyncio

import aiohttp
import httpx
import requests
import time

start_time = time.time()


async def fetch_url(session, url, queue):
    try:
        start_time = time.time()
        async with session.get(url) as response:
            data = await response.text()
            end_time = time.time()
            await queue.put((url, data, start_time, end_time))
    except Exception as e:
        print(f"Ошибка при запросе к {url}: {e}")


async def main():
    queue = asyncio.Queue()
    tasks = []
    async with aiohttp.ClientSession() as session:
        task = fetch_url(session, 'https://api.sampleapis.com/futurama/info', queue)
        tasks.append(task)
        task = fetch_url(session, 'https://www.cbr-xml-daily.ru/latest.js', queue)
        tasks.append(task)
        task = fetch_url(session, 'https://api.sampleapis.com/coffee/hot', queue)
        tasks.append(task)
        await asyncio.gather(*tasks)
        print(queue)


    # Обработка ответов в порядке их быстрейшего получения
    responses = []
    while not queue.empty():
        url, response_data, start_time, end_time = await queue.get()
        response_time = end_time - start_time
        print(f"Ответ из {url} (время выполнения: {response_time:.2f} сек):")
        responses.append(response_data)




asyncio.run(main())



end_time = time.time()
work_time = round(end_time - start_time, 1)
print('total lime:', work_time)