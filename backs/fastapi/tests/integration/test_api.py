from starlette import status

from _version import __version__
from fastapi.testclient import TestClient


def describe_api() -> None:
    def it_should_return_open_api_ui(client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == status.HTTP_200_OK
        assert response.headers["content-type"] == "text/html; charset=utf-8"

    def it_should_return_open_api_json(client: TestClient) -> None:
        response = client.get("/openapi.json")
        open_api_json = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert open_api_json["openapi"] == "3.0.2"
        assert open_api_json["info"]["title"] == "POCemon API"
        assert open_api_json["info"]["version"] == __version__

    def it_should_return_404(client: TestClient) -> None:
        response = client.get("/unknown")
        assert response.status_code == 404
