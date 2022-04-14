from enum import auto

from fastapi_utils.enums import CamelStrEnum


class Type(CamelStrEnum):
    Normal = auto()
    Fire = auto()
    Water = auto()
    Grass = auto()
    Flying = auto()
    Fighting = auto()
    Poison = auto()
    Electric = auto()
    Ground = auto()
    Rock = auto()
    Psychic = auto()
    Ice = auto()
    Bug = auto()
    Ghost = auto()
    Steel = auto()
    Dragon = auto()
    Dark = auto()
    Fairy = auto()
