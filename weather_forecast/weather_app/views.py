import requests
from django.shortcuts import render
from urllib.request import urlopen
import json


API_KEY = 'f45f0c10232d420f8134fffa85b54df7'
IP = '213.134.163.62'

def index(request):
    try:
        location_data = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={IP}').json()
        # getting city from user through input
        city = request.GET.get('city', '')

        # getting city from user through 'locate me' func
        location_data = requests.get('http://ipinfo.io/json').json()
        if 'get_my_city' in request.POST:
            city = location_data['city']

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=86104ffb6aaa5ce42e36c1c32a57ddf0'
        resp = requests.get(url).json()
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
    except (KeyError, TypeError):
        return render(request, 'weather_app/index.html')


