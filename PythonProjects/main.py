import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '460b6943ed23e0a88160daeac30a2096'
HEADER = {'Content_Type' : 'application/json', 'trainer_token' : TOKEN}
Body_Create_a_Pokemon = {
    "name": "Toda",
    "photo_id": 333
}

Body_Change = {
    "pokemon_id": "160799",
    "name": "Toranaga",
    "photo_id": 333
}

Body_Catch = {
    "pokemon_id": "160799"
}

# response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = Body_Create_a_Pokemon)
# print(response_create.status_code)

# response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = Body_Change)
# print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = Body_Change)
print(response_catch.text)