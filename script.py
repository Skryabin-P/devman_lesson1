import requests


def get_weather_forecast(city: str, lang: str = 'ru'):
    url = f'https://wttr.in/{city}?nTqmM&lang={lang}'
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    print(get_weather_forecast('Лондон'))
    print(get_weather_forecast('Шереметьево'))
    print(get_weather_forecast('Череповец'))
