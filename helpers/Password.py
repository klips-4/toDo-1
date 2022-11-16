import hashlib
import uuid
import string
import random


class Password:
    """
    Класс для работы с паролями и хешами
    """
    def __init__(self):
        self._salt = uuid.uuid4().hex

    def get_hash(self, password: str) -> str:
        """
        Метод создания хеша пароля
        :param password: пароль пользователя
        :return: Хеш пароля с солью
        """
        return hashlib.sha256(self._salt.encode() + password.encode()).hexdigest() + ':' + self._salt

    @staticmethod
    def check_hash(hashed_password: str, user_password: str) -> bool:
        """
        проверка совпадения  хешированного и переданного пароля
        :param hashed_password: Хешированный пароль
        :param password: Открытый пароль
        :return: Результат сравненя
        """
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
