from typing import List, Optional

from sqlalchemy.orm import Session

import src.models.team as models
import src.schemas.team as schemas


class TeamService:
    @staticmethod
    def list(db: Session, page: int, page_size: int) -> List[models.Team]:
        return (
            db.query(models.Team).limit(page_size).offset((page - 1) * page_size).all()
        )

    @staticmethod
    def get(db: Session, id: int) -> Optional[models.Team]:
        return db.query(models.Team).filter(models.Team.id == id).first()

    @staticmethod
    def create(db: Session, team: schemas.TeamSave) -> models.Team:
        db_team = models.Team(**team.dict())
        db.add(db_team)
        db.commit()
        db.refresh(db_team)
        return db_team

    @staticmethod
    def update(
        db: Session, team: models.Team, updates: schemas.TeamSave
    ) -> models.Team:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(team, key, value)

        db.commit()
        db.refresh(team)
        return team

    @staticmethod
    def delete(db: Session, team: models.Team) -> None:
        db.delete(team)
        db.commit()
