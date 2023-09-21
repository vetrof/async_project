from django.db import models


class WeatherData(models.Model):
    data = models.TextField()
