import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'afc0606cf78ca82a542de65254c2dcb6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '17906'

def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json ()["data"][0]['trainer_name'] =='Кот'