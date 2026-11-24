"""Educational request examples. Importing this module sends no requests."""

import os

import requests

URL = "https://api.pokemonbattle.ru/v2"
TIMEOUT = 15


def _request(method, path, payload):
    token = os.environ["POKEMON_API_TOKEN"]
    return requests.request(
        method,
        f"{URL}{path}",
        headers={"Content-Type": "application/json", "trainer_token": token},
        json=payload,
        timeout=TIMEOUT,
    )


def register_trainer(email, password):
    return _request(
        "POST",
        "/trainers/reg",
        {
            "trainer_token": os.environ["POKEMON_API_TOKEN"],
            "email": email,
            "password": password,
            "password_re": password,
        },
    )


def confirm_email():
    return _request(
        "POST", "/trainers/confirm_email",
        {"trainer_token": os.environ["POKEMON_API_TOKEN"]},
    )


def create_pokemon(name, photo_id):
    return _request("POST", "/pokemons", {"name": name, "photo_id": photo_id})


def change_pokemon(pokemon_id, name, photo_id):
    return _request(
        "PUT", "/pokemons",
        {"pokemon_id": pokemon_id, "name": name, "photo_id": photo_id},
    )


def add_to_pokeball(pokemon_id):
    return _request("POST", "/trainers/add_pokeball", {"pokemon_id": pokemon_id})
