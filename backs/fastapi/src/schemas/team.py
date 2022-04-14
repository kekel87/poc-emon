from typing import Optional

from src.schemas.base import BaseSchema


# Shared properties
class TeamBase(BaseSchema):
    name: str
    owner: str
    pokemon_1: int
    pokemon_2: Optional[int]
    pokemon_3: Optional[int]
    pokemon_4: Optional[int]
    pokemon_5: Optional[int]
    pokemon_6: Optional[int]


# Properties to receive via API on creation
# Properties to receive via API on update
class TeamSave(TeamBase):
    pass


# Additional properties stored in DB
class TeamInDb(TeamBase):
    id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Team(TeamInDb):
    pass
