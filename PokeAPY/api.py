import requests
import json

from PokeAPY.models import (Pokemon,
                            Move)
from PokeAPY.utils import format_name


class PokeAPI:
    def __init__(self, base_url='https://pokeapi.co/api/v2/') -> None:
        self.base_url = base_url

    def get_pokemon(self, name_or_id: str) -> Pokemon:
        response = requests.get(f"{self.base_url}pokemon/{name_or_id}")
        if response.status_code == 200:
            data = response.json()
            return Pokemon(
                id=data['id'],
                name=format_name(data['name']),
                height=data['height'],
                weight=data['weight'],
                types=[
                    format_name(type['type']['name']) for type in data['types']
                ],
                moves=[
                    format_name(move['move']['name']) for move in data['moves']
                ],
                abilities=[
                    format_name(ability['ability']['name']) for ability in data['abilities']
                ],
                stats=[
                    {stat['stat']['name']: stat['base_stat']}
                    for stat in data['stats']
                ],
                sprites=data['sprites']
            )
        else:
            response.raise_for_status()

    def get_move(self, name_or_id: str) -> json:
        response = requests.get(f"{self.base_url}move/{name_or_id}")
        if response.status_code == 200:
            data = response.json()
            return Move(
                name=format_name(data['name']),
                accuracy=data['accuracy'],
                power=data['power'],
                pp=data['pp'],
                priority=data['priority'],
                type=data['type']['name'],
                damage_class=data['damage_class']['name'],
                learned_by=[
                    format_name(pokemon['name']) for pokemon in data['learned_by_pokemon']
                ]
            )
        else:
            response.raise_for_status()
