import datetime
from typing import Optional, List

from pydantic import BaseModel

from models.utils import AuditBase, IdBase, PaginationBase


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


class ItemIn(ItemBase):
    pass


class ItemOut(ItemBase, IdBase):
    pass


class ItemPagination(PaginationBase[ItemOut]):
    pass


class ItemInDB(ItemBase, IdBase, AuditBase):
    pass
