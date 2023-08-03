import requests
from django.shortcuts import render
from urllib.request import urlopen
import json


def index(request):
    location_data = requests.get('http://ipinfo.io/json').json()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=86104ffb6aaa5ce42e36c1c32a57ddf0'
    city = request.GET.get('city', 'Warsaw')

    if 'get_my_city' in request.POST:
        city = location_data['city']
    resp = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': resp['main']['temp'],
        'temp_max': resp['main']['temp_max'],
        'temp_min': resp['main']['temp_min'],
        'description': resp['weather'][0]['description'],
        'feels_like': resp['main']['feels_like'],
        'icon': resp['weather'][0]['icon'],
    }

    context = {'city_info': city_info}
    return render(request, 'weather_app/index.html', context)

