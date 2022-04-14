from fastapi_utils.camelcase import snake2camel
from pydantic import BaseConfig, BaseModel


def snake_2_camel(m: str) -> str:
    return snake2camel(m, True)


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = snake_2_camel
