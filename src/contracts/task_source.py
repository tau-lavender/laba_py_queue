from src.contracts.task import Task
from typing import Iterable, Protocol, runtime_checkable


@runtime_checkable
class TaskSource(Protocol):
    """
    Протокол источника задач
    """

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач
        :return: задачи класса Task в итерируемом объекте
        """
        ...
