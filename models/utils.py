import datetime
from typing import TypeVar, List, Generic

from pydantic import BaseModel

T = TypeVar('T')


class AuditBase(BaseModel):
    created_date: datetime
    created_by: str
    updated_date: datetime
    updated_by: str


class IdBase(BaseModel):
    id: str


class PaginationBase(BaseModel, Generic[T]):
    total: int
    offset: int
    limit: int
    data: List[T]
