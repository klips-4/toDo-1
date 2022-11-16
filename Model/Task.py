from Model.BaseModel import BaseModel

from sqlalchemy import Column, Text, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Task(BaseModel):
    __tablename__ = 'tasks'

    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(Text, nullable=False)
    date_completed = Column(DateTime)

    user = relationship('User',
                        foreign_keys=[user_id])
