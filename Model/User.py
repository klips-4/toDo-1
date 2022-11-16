from Model.BaseModel import BaseModel
from helpers.Password import Password

from sqlalchemy import Column, Text, DateTime, ForeignKey, Integer


class User(BaseModel):
    __tablename__ = 'users'

    _guarded = ['password']
    _manual_fillable = ['password']

    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    login = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)

    def _manual_fillable_fields(self, record: dict):
        if record.get('password') and not record.get('id'):
            self.password = Password().get_hash(record.get('password'))
