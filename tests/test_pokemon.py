import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers'
           )
    assert response.status_code == 200

def test_parametrize():
    response = requests.get(url=f'{HOST}/trainers', 
              params= {'trainer_id': 3733}
           )
    assert response.json()['trainer_name'] == 'Виола' 