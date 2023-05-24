import requests

# Separate the data from the API
EN_PAYLOAD = {'lang': 'en'}
RU_PAYLOAD = {'lang': 'ru'}
PLACES = {
    'London': 'https://wttr.in/london?nTqu',
    'SVO': 'https://wttr.in/svo?nTqu',
    'Череповец': 'https://wttr.in/Череповец',
}

for place, url in PLACES.items():
    payload = RU_PAYLOAD if place == 'Череповец' else EN_PAYLOAD
    response = requests.get(f'{url}?MnqT' if place == 'Череповец' else url, params=payload)
    response.raise_for_status()
    print(response.text)