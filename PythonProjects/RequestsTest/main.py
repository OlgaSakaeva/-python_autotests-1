import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '26adc5b5a9344312b57964363eb5f84e'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN
          }
body_registration = {
 "name": "generate",
 "photo_id": -1
}

body_change_name = {
     "pokemon_id": "369551",
    "name": "testPython2",
    "photo_id": 2
}

body_inpokeball = {
     "pokemon_id": "369553"
}

response =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration )
print(response.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name )
print(response_change_name.text)

response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_inpokeball )
print(response_inpokeball.text)