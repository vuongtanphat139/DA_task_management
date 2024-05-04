from sqlalchemy import Column, Integer, String, DateTime, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'CATEGORY'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"Category('{self.name}', '{self.date_created}')"