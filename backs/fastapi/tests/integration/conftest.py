from typing import Generator

import pytest
from utils import database

from fastapi.testclient import TestClient
from src.core.settings import Settings

"""
This global var it is used for reset database after tests that modify it.
This saves a lot of time on tests that only read (typically GET).
See run_before_and_after_tests function.
"""
pytest.reset_db_after_test = False


@pytest.fixture(scope="session", autouse=True)
def set_database(settings: Settings) -> Generator[None, None, None]:
    """
    Start and prepare for integration tests
    """
    database.prepare(settings)

    yield

    database.remove()


@pytest.fixture(autouse=True)
def run_before_and_after_tests(settings: Settings) -> Generator[None, None, None]:
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want
    if pytest.reset_db_after_test:
        pytest.reset_db_after_test = False
        database.reset(settings)


@pytest.fixture
def client(settings: Settings) -> TestClient:
    """
    Test client for integration tests
    """
    from main import get_application  # type: ignore

    app = get_application()
    client = TestClient(app, base_url="http://testserver")

    return client
