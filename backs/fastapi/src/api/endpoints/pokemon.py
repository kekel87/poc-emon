from typing import List

from sqlalchemy.orm import Session
from starlette import status

import src.models.pokemon as model
import src.schemas.pokemon as schema
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from src.api.dependencies.db_session import db_session
from src.services.pokemon_service import PokemonService

router = APIRouter()


@router.get(
    "",
    response_model=List[schema.Pokemon],
    summary="List pokemons",
    description="List pokemons, with pagination and ordered",
    response_model_exclude_none=True,
)
def list(
    db: Session = Depends(db_session),
    page: int = Query(0, description="Page to display"),
    page_size: int = Query(10, description="Number of pokemon per page"),
) -> List[model.Pokemon]:
    return PokemonService.list(db, page, page_size)


@router.get(
    "/{id}",
    response_model=schema.Pokemon,
    responses={404: {}},
    summary="Get one pokemon",
    description="Returns a specific pokemon, with all this information",
    response_model_exclude_none=True,
)
def get(
    db: Session = Depends(db_session),
    id: int = Path(..., description="Pokemon id"),
) -> model.Pokemon:
    pkm = PokemonService.get(db, id)

    if pkm is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return pkm
