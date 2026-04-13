from dataclasses import dataclass
from datetime import datetime
from itertools import count
from typing import Any

from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum, TRANSITIONS

'''
Атрибуты задачи:
- идентификатор задачи
- описание задачи
- приоритет
- статус задачи
- время создания
'''


@dataclass(slots=True)
class Task(object):
    """
    Task dataclass
    Хранит данные о задаче
    Имеет чистый защищённый API
    """
    __payload: Any
    __priority: PriorityEnum
    __status: StatusEnum

    __creation_time: datetime
    __id: int
    _id_counter = count(0)

    def __init__(self,
                 payload: object = None,
                 priority: PriorityEnum = PriorityEnum.NORMAL,
                 status: StatusEnum = StatusEnum.SCHEDULED):
        if payload is None:
            raise ValueError("Payload cannot be None")
        if not isinstance(priority, PriorityEnum):
            raise ValueError(f"Priority ({priority}) must be from priority enum")
        if not isinstance(status, StatusEnum):
            raise ValueError(f"Status ({status}) must be from status enum")

        self.__payload = payload
        self.__priority = priority
        self.__status = status

        self.__id = next(Task._id_counter)
        self.__creation_time = datetime.now()

    @property
    def payload(self) -> object:
        return str(self.__payload) if self.__payload is not None else ""

    @payload.setter
    def payload(self, value) -> None:
        if hasattr(self, "__payload") and self.__payload is not None:
            raise AttributeError("Payload allready set")
        if not isinstance(value, (list, int, str)):
            raise TypeError("Payload must be list, int or set")
        self.__payload = value

    @property
    def priority(self) -> PriorityEnum:
        return self.__priority

    @property
    def status(self) -> StatusEnum:
        return self.__status

    @status.setter
    def status(self, value: StatusEnum) -> None:
        if not isinstance(value, StatusEnum):
            raise ValueError(f"Status ({value}) must be from status enum")
        if value in TRANSITIONS[self.__status]:
            self.__status = value
        else:
            raise ValueError(f"Impossible to set from {self.__status} to {value}")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def creation_time(self) -> datetime:
        return self.__creation_time
