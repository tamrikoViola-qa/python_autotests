import requests


# response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
#               json={
#     "name": "Pikachuha",
#     "photo": "https://dolnikov.ru/pokemons/albums/011.png"
#     }, 
#     headers= {'Content-Type': 'application/json',
#              'trainer_token': '328a31ce135a787c8ec05d4c222d0f1a'}
#            )
# print(response)
#TODO Закоментила создание покемона

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
    "pokemon_id": "21362",
    "name": "Listovik10",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
    }, 
    headers= {'Content-Type': 'application/json',
             'trainer_token': '328a31ce135a787c8ec05d4c222d0f1a'}
           )
print(response)

response = requests.post(url='https://api.pokemonbattle.me:9104//trainers/add_pokeball', 
              json={
    "pokemon_id": "21362",
   }, 
    headers= {'Content-Type': 'application/json',
             'trainer_token': '328a31ce135a787c8ec05d4c222d0f1a'}
           )
print(response)