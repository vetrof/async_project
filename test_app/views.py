import requests
from django.http import JsonResponse
from django.shortcuts import render
import time


def home(request):
    games = {}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        games = requests.get('https://api.sampleapis.com/switch/games').json()
        return JsonResponse({'games': games})

    return render(request, 'weather_ajax_get_data.html', {'games': games})


def home2(request):
    weather = {}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        weather = requests.get('https://feelweather.click/api/astana').json()
        return JsonResponse({'weather': weather})

    return render(request, 'weather_ajax_button.html', {'weather': weather})


def home3(request):
    weather = requests.get('https://feelweather.click/api/astana').json()
    return render(request, '3.html', {'weather': weather})

