from typing import List, cast

from sqlalchemy.orm import Session

import src.models.pokemon as models


class PokemonService:
    @staticmethod
    def list(db: Session, page: int, page_size: int) -> List[models.Pokemon]:
        return cast(
            List[models.Pokemon],
            (
                db.query(models.Pokemon)
                .limit(page_size)
                .offset((page - 1) * page_size)
                .all()
            ),
        )

    @staticmethod
    def get(db: Session, id: int) -> models.Pokemon:
        return cast(models.Pokemon, db.query(models.Pokemon).get(id))
