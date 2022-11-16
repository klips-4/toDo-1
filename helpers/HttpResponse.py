from typing import Optional, Union

from flask import make_response


class HttpResponse:
    @staticmethod
    def make(*, data: Optional[Union[int, float, str, bool, dict, list]] = None,
             success: Optional[bool] = True,
             meta: Optional[dict] = None,
             error_text: Optional[str] = None):
        """
        Метод стандартизованного ответа

        :param data:  Данные для ответа
        :param success: Признак успешности запроса
        :param meta: Мета данные
        :param error_text:  текст ошибки
        :return: Стандартизованные ответы для сетевого взаимодействия
        """
        return make_response({
            'data': data,
            'success': success,
            'meta': meta,
            'error_text': error_text
        })
