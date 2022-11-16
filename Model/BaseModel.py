from sqlalchemy import Column, Integer, DateTime

from app import Model, engine
from sqlalchemy.orm import declarative_mixin

from typing import List

import datetime


@declarative_mixin
class BaseModel(Model):
    __abstract__ = True


    _guarded: List[str] = []
    _fillable: List[str] = []
    _manual_fillable: List[str] = []

    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    @property
    def session(self):
        return engine.session

    def from_object(self, record: dict, create_method: bool = False):
        """
        Создание модели из словаря

        :param record: Запись - словарь с данными
        """

        fields = self._get_fillable_fields()

        for field in fields:
            if field.key in record:
                setattr(self, field.key, record.get(field.key))

        if not self.created_at:
            self.created_at = datetime.datetime.now()
        else:
            self.updated_at = datetime.datetime.now()

        if not create_method:
            self._manual_fillable_fields(record)

        return self

    def to_dict(self) -> dict:
        """
        Преобразование модели в словарь
        :return: Словарь с данными из модели
        """

        result = {}

        columns = self._get_columns()

        for column_name in columns:
            result[column_name.key] = getattr(self, column_name.key)

        self._manual_response_fields(result)

        return result

    def add_default_data(self):

        """
        Добавление начальных данных
        """
        pass

    def _manual_fillable_fields(self, record: dict):
        """
        Ручное заполнение модели перед сохранением
        """
        pass

    def _manual_response_fields(self, result: dict):
        """
        Заполнение полей перед ответом
        """
        pass

    def _get_columns(self) -> List[str]:
        """
        Получение списка колонок, которые получаются из модели
        :return: список колонок для метода to_dict
        """
        return self._get_columns_name(self._guarded)

    def _get_fillable_fields(self) -> List[str]:

        """
        Получеине списка полей для заполнения
        :return: список полей для автоматического заполнения в модели

        """
        return self._get_columns_name(self._manual_fillable)

    def _get_columns_name(self, skip_fields: List[str]) -> List[str]:

        """
        Получение списка полей, которые не содержатся в skip_fields
        :param skip_fields: Пропускаемые поля
        :return: список полей без учета skip_fields

        """
        columns = self.metadata.tables.get(self.__tablename__).columns

        if columns:
            return [column_name for column_name in columns
                    if column_name not in skip_fields]

        return []
