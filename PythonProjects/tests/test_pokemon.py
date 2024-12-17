import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '460b6943ed23e0a88160daeac30a2096'
HEADER = {'Content_Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_id = '19709'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_id})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_id})
    assert response.json()["data"][0]["trainer_name"] == "Кафка"