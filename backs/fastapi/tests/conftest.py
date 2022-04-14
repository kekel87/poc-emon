import pytest

from src.core.settings import Settings
from src.core.settings import settings as get_settings

Settings.Config.env_file = "tests/.env"


@pytest.fixture(scope="session")
def settings() -> Settings:
    return get_settings()
