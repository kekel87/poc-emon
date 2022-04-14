from mocks import pokemon
from starlette import status

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient


def describe_list_pokemons() -> None:
    def it_should_list_default(client: TestClient) -> None:
        response = client.get("/pokemons")
        assert response.status_code == status.HTTP_200_OK

        pokemons = response.json()
        assert len(pokemons) == 10
        assert pokemons[0] == jsonable_encoder(pokemon.base)

    def it_should_list_with_paginated(client: TestClient) -> None:
        page = 10
        page_size = 20
        response = client.get(f"/pokemons?page={page}&page_size={page_size}")
        assert response.status_code == status.HTTP_200_OK

        pokemons = response.json()
        assert len(pokemons) == 20
        assert pokemons[0].get("id") == (page - 1) * page_size + 1


def describe_get_pokemon() -> None:
    def it_should_obtain_pokemon(client: TestClient) -> None:
        response = client.get("/pokemons/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == jsonable_encoder(pokemon.base)

    def it_should_return_not_found(client: TestClient) -> None:
        response = client.get("/pokemons/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND
