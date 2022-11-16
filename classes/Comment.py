from classes.BaseClass import BaseClass
from Model.Comment import Comment as CommentModel


class Comment(BaseClass):
    @staticmethod
    def _get_model(new_model: bool = False) -> CommentModel:
        return CommentModel() if new_model else CommentModel
