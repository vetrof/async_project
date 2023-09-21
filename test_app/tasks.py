import asyncio
import httpx
from django.db import transaction
from test_app.models import WeatherData

async def fetch_weather_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('feelweather.click/api/astana')
        return response.json()

async def update_weather_forecast():
    while True:
        weather_data = await fetch_weather_data()

        # Сохраняем данные о погоде в базе данных (предположим, что есть модель WeatherData)
        # with transaction.atomic():
        #     WeatherData.objects.create(
        #         temperature=weather_data['temperature'],
        #         conditions=weather_data['conditions'],
        #         timestamp=weather_data['timestamp']
        #     )

        # Пауза на 1 час
        await asyncio.sleep(3600)
