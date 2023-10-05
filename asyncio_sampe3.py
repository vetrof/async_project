import asyncio
import time
import aiohttp
start = time.time()
async def futurama():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.sampleapis.com/futurama/info') as response:
            data = await response.text()
            end = time.time()
            print("Функция futurama завершила запрос за:", end - start)


async def latest():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.cbr-xml-daily.ru/latest.js') as response:
            data = await response.text()
            end = time.time()
            print("Функция latest завершила запрос за:", end - start)
            # print(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [futurama(), latest()]
    loop.run_until_complete(asyncio.gather(*tasks))


end = time.time()
print("общее время:", end - start)
