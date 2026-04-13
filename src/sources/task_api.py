import time
import random
from typing import Iterable
from src.contracts.task import Task
from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum


class TaskSourceAPI:
    """
    Источник задач - API заглушка
    """

    def __init__(self) -> None:
        self.fake_data = ["task from api", "another task from api", "abababa"]

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач соответствующий протоколу TaskSource
        """
        for i in range(len(self.fake_data)):
            time.sleep(random.randint(1, 4))
            yield Task(self.fake_data[i],
                       priority=random.choice([PriorityEnum.SUPER_HIGH, PriorityEnum.HIGH, PriorityEnum.NORMAL, PriorityEnum.LOW, PriorityEnum.SUPER_LOW]),
                       status=random.choice([StatusEnum.SCHEDULED, StatusEnum.ERROR, StatusEnum.COMPLETED]))
