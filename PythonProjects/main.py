import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'afc0606cf78ca82a542de65254c2dcb6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "199546",
    "name": "Покемон",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "201210"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)
message = response_create.json()['message']
print (message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (response_change.text)
message = response_change.json()['message']
print (message)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print (response_pokeball.text)
message = response_pokeball.json()['message']
print (message)