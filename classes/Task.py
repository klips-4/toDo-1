from classes.BaseClass import BaseClass
from Model.Task import Task as TaskModel


class Task(BaseClass):
    __tablename__ = 'tasks'

    @staticmethod
    def _get_model(new_model: bool = False) -> TaskModel:
        return TaskModel() if new_model else TaskModel

    def _prepare_query_filter(self, query, filter_params):
        if filter_params:
            filter_params = {}

        if filter_params.get('onlyActive'):
            query = query.where(self.get_model().date_completed == None)

        if filter_params.get('onlyCompleted') and not filter_params.get('onlyActive'):
            query = query.where(self.get_model().date_completed != None)

        return query
