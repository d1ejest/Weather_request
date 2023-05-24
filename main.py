import requests


def main():
    url_temp = 'https://wttr.in/{}'
    playload = {'lang': 'ru',
                'M': '', ''
                         'n': '',
                'q': '',
                'T': ''}
    PLACES = ['Лондон', 'Шереметьево', 'Череповец']

    for place in PLACES:
        url = url_temp.format(place)
        response = requests.get(url, params=playload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
