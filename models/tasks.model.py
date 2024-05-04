from sqlalchemy import Column, Integer, String, DateTime, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'TASK'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(400), nullable=False)
    start_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)
    category_id = Column(Integer, ForeignKey('CATEGORY.id'), nullable=False)
    category = relationship("Category", backref="tasks")
    finished_date = Column(Date)
    status = Column(Enum('TODO', 'IN PROGRESS', 'FINISHED'))

    def __repr__(self):
        return f"Task('{self.name}', '{self.description}', '{self.start_date}', '{self.due_date}', '{self.category_id}')"