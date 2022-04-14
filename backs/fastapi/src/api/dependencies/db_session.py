from typing import Generator

from sqlalchemy.orm import Session

from src.core.database import SessionLocal


def db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
