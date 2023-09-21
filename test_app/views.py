import requests
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    weather = {}
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        weather = requests.get('https://feelweather.click/api/astana').json()
        return JsonResponse({'weather': weather})
    else:
        return render(request, 'home.html', {'weather': weather})

