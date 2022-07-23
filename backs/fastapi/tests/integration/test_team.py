import pytest
from mocks import team
from starlette import status

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient


def describe_list() -> None:
    def it_should_list_default(client: TestClient) -> None:
        response = client.get("/teams")
        assert response.status_code == status.HTTP_200_OK

        teams = response.json()
        assert len(teams) == 1
        assert teams[0] == jsonable_encoder(team.base)

    def it_should_list_with_paginated(client: TestClient) -> None:
        page = 10
        page_size = 20
        response = client.get(f"/teams?page={page}&page_size={page_size}")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0


def describe_create() -> None:
    def it_should_create_new_team(client: TestClient) -> None:
        pytest.reset_db_after_test = True
        response = client.post("/teams", json=jsonable_encoder(team.save))

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            "id": 2,
            **jsonable_encoder(team.save, exclude_none=True),
        }

        response = client.get("/teams")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2


def describe_get() -> None:
    def it_should_obtain_team(client: TestClient) -> None:
        response = client.get("/teams/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == jsonable_encoder(team.base, exclude_none=True)

    def it_should_return_not_found(client: TestClient) -> None:
        response = client.get("/teams/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND


def describe_update() -> None:
    def it_should_update_existing_team(client: TestClient) -> None:
        pytest.reset_db_after_test = True
        response = client.put("/teams/1", json=jsonable_encoder(team.save))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": 1,
            **jsonable_encoder(team.save, exclude_none=True),
        }

    def it_should_return_not_found(client: TestClient) -> None:
        response = client.put("/teams/99999", json=jsonable_encoder(team.save))
        assert response.status_code == status.HTTP_404_NOT_FOUND


def describe_delete() -> None:
    def it_should_delete_existing_team(client: TestClient) -> None:
        pytest.reset_db_after_test = True
        response = client.delete("/teams/1")
        assert response.status_code == status.HTTP_200_OK

        response = client.get("/teams")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def it_should_return_not_found(client: TestClient) -> None:
        response = client.delete("/teams/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND
