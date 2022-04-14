from typing import List

from sqlalchemy.orm import Session
from starlette import status

import src.models.team as model
import src.schemas.team as schema
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from src.api.dependencies.db_session import db_session
from src.services.team_service import TeamService

router = APIRouter()


@router.get("", summary="List all teams", response_model=List[schema.Team])
def list(
    page: int = Query(0, description="Page to display"),
    page_size: int = Query(10, description="Number of team per page"),
    db: Session = Depends(db_session),
) -> List[model.Team]:
    return TeamService.list(db, page, page_size)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create a team",
    description="Create a new team, with a maximum of 6 pokemon and un minim of 1.",
    response_model=schema.Team,
)
def create(
    team: schema.TeamSave = Body(...),
    db: Session = Depends(db_session),
) -> model.Team:
    return TeamService.create(db, team)


@router.get("/{id}", summary="Get a team", response_model=schema.Team)
def get(
    id: int = Path(...),
    db: Session = Depends(db_session),
) -> model.Team:
    db_team = TeamService.get(db, id)
    if not db_team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return db_team


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Update a team",
    description="Update an existing team.",
    response_model=schema.Team,
)
def update(
    id: int = Path(...),
    team: schema.TeamSave = Body(...),
    db: Session = Depends(db_session),
) -> model.Team:
    db_team = TeamService.get(db, id)
    if not db_team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return TeamService.update(db, db_team, team)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Detele a team",
    description="Detele an existing team.",
)
def delete(
    id: int = Path(...),
    db: Session = Depends(db_session),
) -> None:
    db_team = TeamService.get(db, id)
    if not db_team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return TeamService.delete(db, db_team)
