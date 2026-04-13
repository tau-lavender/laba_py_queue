from enum import Enum


class StatusEnum(Enum):
    """
    Enum для статусов задач
    """
    SCHEDULED = "Scheduled"
    STARTED = "Started"
    COMPLETED = "Completed succesfully"
    ERROR = "Completed with error"
    CANCELLED = "Canceled"


# переходы между статусами
TRANSITIONS = {StatusEnum.SCHEDULED: {StatusEnum.STARTED, StatusEnum.COMPLETED, StatusEnum.ERROR, StatusEnum.CANCELLED},
               StatusEnum.STARTED: {StatusEnum.COMPLETED, StatusEnum.ERROR, StatusEnum.CANCELLED},
               StatusEnum.COMPLETED: {},
               StatusEnum.ERROR: {},
               StatusEnum.CANCELLED: {}}
