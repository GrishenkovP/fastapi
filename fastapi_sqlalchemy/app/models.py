from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class Sale(Base):
    __tablename__ = "Sales"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    city = Column(String(100), index=True)
    manager = Column(String(50), index=True)
    product = Column(String(150), index=True)
    amount = Column(Integer)