from sqlmodel import SQLModel, Field
from typing import Optional


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: Optional[bool] = None
