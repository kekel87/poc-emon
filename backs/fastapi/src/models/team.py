from sqlalchemy import Column, ForeignKey, Integer, String

from src.models.base import Base


class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    owner = Column(String, nullable=False)

    pokemon_1 = Column(Integer, ForeignKey("pokemon.id"), nullable=False)
    pokemon_2 = Column(Integer, ForeignKey("pokemon.id"))
    pokemon_3 = Column(Integer, ForeignKey("pokemon.id"))
    pokemon_4 = Column(Integer, ForeignKey("pokemon.id"))
    pokemon_5 = Column(Integer, ForeignKey("pokemon.id"))
    pokemon_6 = Column(Integer, ForeignKey("pokemon.id"))
