import random
import string
from typing import Iterable
from src.contracts.task import Task
from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum


class TaskSourceGen:
    """
    Источник задач - генератор
    """

    def __init__(self) -> None:
        self.count = random.randint(2, 5)

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач соответствующий протоколу TaskSource
        """
        for i in range(1, self.count + 1):
            yield Task(payload=list(random.choices(string.ascii_lowercase, k=20)),
                       priority=random.choice([PriorityEnum.SUPER_HIGH, PriorityEnum.HIGH, PriorityEnum.NORMAL, PriorityEnum.LOW, PriorityEnum.SUPER_LOW]),
                       status=random.choice([StatusEnum.SCHEDULED, StatusEnum.ERROR, StatusEnum.COMPLETED]))
