import requests

# Separate the data from the API
en_playload = {'lang': 'en'}
ru_playload = {'lang': 'ru'}
places = {'London': 'https://wttr.in/london?nTqu', 'SVO': 'https://wttr.in/svo?nTqu',
          'Череповец': 'https://wttr.in/Череповец'}

for place, url in places.items():
    if place == 'Череповец':
        response = requests.get(url + '?MnqT', params=ru_playload)
    else:
        response = requests.get(url, params=en_playload)
    response.raise_for_status()
    print(response.text)
