"""Educational GET checks for the Pokémon Battle training API."""

import os

import pytest
import requests

URL = "https://api.pokemonbattle.ru/v2"
TIMEOUT = 15


def required_env(name):
    value = os.getenv(name)
    if not value:
        pytest.skip(f"Set {name} to run this test")
    return value


def get_pokemons(trainer_id):
    return requests.get(
        f"{URL}/pokemons", params={"trainer_id": trainer_id}, timeout=TIMEOUT
    )


def find_pokemon(trainer_id, pokemon_id):
    response = get_pokemons(trainer_id)
    assert response.status_code == 200
    for pokemon in response.json()["data"]:
        if str(pokemon["id"]) == pokemon_id:
            return pokemon
    pytest.fail("Configured Pokémon was not found in the returned data")


def test_status_code():
    trainer_id = required_env("POKEMON_TRAINER_ID")
    response = get_pokemons(trainer_id)
    assert response.status_code == 200


def test_part_of_response():
    trainer_id = required_env("POKEMON_TRAINER_ID")
    pokemon_id = required_env("POKEMON_ID")
    expected_name = required_env("POKEMON_NAME")
    assert find_pokemon(trainer_id, pokemon_id)["name"] == expected_name


@pytest.mark.parametrize(
    "key, variable",
    [
        ("name", "POKEMON_NAME"),
        ("trainer_id", "POKEMON_TRAINER_ID"),
        ("id", "POKEMON_ID"),
    ],
)
def test_parametrize(key, variable):
    trainer_id = required_env("POKEMON_TRAINER_ID")
    pokemon_id = required_env("POKEMON_ID")
    expected = required_env(variable)
    assert str(find_pokemon(trainer_id, pokemon_id)[key]) == expected


def test_status_code_trainer():
    response = requests.get(f"{URL}/trainers", timeout=TIMEOUT)
    assert response.status_code == 200


def test_my_trainer():
    trainer_id = required_env("POKEMON_TRAINER_ID")
    expected_name = required_env("POKEMON_TRAINER_NAME")
    response = requests.get(
        f"{URL}/trainers/{trainer_id}",
        params={"trainer_id": trainer_id},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    assert response.json()["trainer_name"] == expected_name
