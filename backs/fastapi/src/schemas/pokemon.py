from typing import Optional

from pydantic import Field

from src.enums.type import Type
from src.schemas.base import BaseSchema


# Shared properties
# Properties to receive via API on creation
# Properties to receive via API on update
# Additional properties stored in DB
# Additional properties to return via API
class Pokemon(BaseSchema):
    id: int = Field(..., description="Pokemon id", example="Bulbasaur")
    name: str = Field(..., description="Pokemon name", example="Bulbasaur")
    type_1: Type
    type_2: Optional[Type]

    class Config:
        orm_mode = True
