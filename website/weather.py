import requests


def get_weather_today(city_id, appid):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': appid})

        data = res.json()
        today_weather = {'city': data['name'],
                         'conditions': data['weather'][0]['description'],
                         'temp': data['main']['temp']}
        return today_weather
    except Exception:
        return 0
