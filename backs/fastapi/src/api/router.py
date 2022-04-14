from fastapi import APIRouter
from src.api.endpoints import pokemon, team

router = APIRouter()

router.include_router(pokemon.router, prefix="/pokemons", tags=["pokemon"])
router.include_router(team.router, prefix="/teams", tags=["team"])
