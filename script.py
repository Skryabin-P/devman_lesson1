import requests


def get_weather_forecast(city: str, lang: str = 'ru'):
    url = f'https://wttr.in/{city}'
    payload = {"nTqmM": "","lang": lang}
    response = requests.get(url,params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    cities_list = ['Лондон','Шереметьево','Череповец']
    for city in cities_list:
        try:
            print(get_weather_forecast(city))
        except requests.exceptions.HTTPError as error:
            exit(f"Can't fetch the data from the remote host: \n {error}")


