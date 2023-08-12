import requests
from pprint import pprint

API_KEY = 'f45f0c10232d420f8134fffa85b54df7'
IP = '213.134.163.62'
location_data = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={IP}').json()

info = {
    'country_name': location_data['country_name'],
    'city': location_data['city'],
    'current_time': location_data['time_zone']['current_time'][11:19],
    'country_flag': location_data['country_flag'],
}

pprint(location_data)