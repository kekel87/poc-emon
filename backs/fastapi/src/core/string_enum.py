from __future__ import annotations

from enum import Enum
from typing import Any

from fastapi_utils.camelcase import camel2snake
from sqlalchemy import Enum as SqlalchemyEnum
from sqlalchemy import TypeDecorator


class StringEnum(TypeDecorator[Enum]):
    """
    This TypeDecorator implement sqlalchemy `Enum` and tell it to use values instead of
    keys.

    See https://newbedev.com/best-way-to-do-enum-in-sqlalchemy
    See https://michaelcho.me/article/using-python-enums-in-sqlalchemy-models
    """

    impl = SqlalchemyEnum

    cache_ok = True

    def __init__(self, enum: Any):
        super().__init__(*[e.value for e in enum], name=camel2snake(enum.__name__))
        self.enum = enum

    def copy(self, **_: Any) -> StringEnum:
        return StringEnum(self.enum)

    def process_bind_param(self, value: Any, dialect: Any) -> Any:
        if value is None:
            return None
        return value.value

    def process_result_value(self, value: Any, dialect: Any) -> Any:
        if value is None:
            return None
        return self.enum(value)
