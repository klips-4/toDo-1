from classes.BaseClass import BaseClass
from Model.User import User as UserModel
from helpers.HttpResponse import HttpResponse
from helpers.Password import Password


class User(BaseClass):
    __tablename__ = 'users'

    def __init__(self):
        self._additional_methods = {
            'Login': self.login
        }

        super().__init__()

    @staticmethod
    def _get_model(new_model: bool = False) -> UserModel:
        return UserModel() if new_model else UserModel

    def login(self, **kwargs):
        """
        Метод проверки введенных данных
        :param kwargs: Данные введенные пользоваелем
        :return: Результат запроса
        """
        data = kwargs.get('data')
        login = data.get('login')
        password = data.get('password')

        if not login:
            return HttpResponse.make(success=False, error_text='Не передан логин')

        if not password:
            return HttpResponse.make(success=False, error_text='Не передан пароль')

        user = self._session.query(self._get_model()).filter(self._get_model().login == login)

        if user and user.count():
            user = user.first()

            if Password.check_hash(user.password, password):
                return HttpResponse.make(data=user.to_dict())
            else:
                return HttpResponse.make(success=False, error_text='Неверный пароль')

        else:
            return HttpResponse.make(success=False, error_text='Логин не найден')
