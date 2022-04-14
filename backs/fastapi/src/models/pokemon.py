from sqlalchemy import Column, Integer, String

from src.core.string_enum import StringEnum
from src.enums.type import Type
from src.models.base import Base


class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    type_1 = Column(StringEnum(Type), nullable=False)
    type_2 = Column(StringEnum(Type))
