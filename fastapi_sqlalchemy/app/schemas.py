from datetime import date
from pydantic import BaseModel


class Sale(BaseModel):
    id: int
    date: date
    city: str
    manager: str
    product: str
    amount: int

    class Config:
        orm_mode = True