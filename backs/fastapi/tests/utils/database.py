import os

from mocks import team
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from alembic.command import upgrade
from alembic.config import Config
from src.core.settings import Settings
from src.models.team import Team


def prepare(settings: Settings) -> None:
    __run_migration()
    print("\nInsert initial data")
    __initial_data(settings.sqlalchemy_database_url)


def remove() -> None:
    os.remove("test.sqlite")


def reset(settings: Settings) -> None:
    __truncate(settings.sqlalchemy_database_url)
    __initial_data(settings.sqlalchemy_database_url)


def __run_migration() -> None:
    print("\nPrepare database")
    print("\nRun Alembic migration")
    upgrade(Config(file_=os.path.realpath("alembic.ini")), "head")


def __truncate(url: str) -> None:
    engine = create_engine(url)

    meta = MetaData()
    meta.reflect(bind=engine)

    con = engine.connect()
    trans = con.begin()

    for table in meta.sorted_tables:
        con.execute(table.delete())

    trans.commit()
    engine.dispose()


def __initial_data(url: str) -> None:
    engine = create_engine(url)
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

    db.add(Team(**team.db))

    db.commit()
    db.close()
