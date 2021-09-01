import datetime
from typing import TypeVar, List, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')


class AuditBase:
    created_date: datetime
    created_by: str
    updated_date: datetime
    updated_by: str


class IdBase:
    id: str


class PaginationBase(GenericModel, Generic[T]):
    total: int
    offset: int
    limit: int
    data: List[T]
