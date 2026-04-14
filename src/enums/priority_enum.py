from enum import IntEnum


class PriorityEnum(IntEnum):
    """
    Enum для приоритетов задач
    """
    SUPER_HIGH = 5
    HIGH = 4
    NORMAL = 3
    LOW = 2
    SUPER_LOW = 1


PRIORITY_ENUM_ORDER: list[PriorityEnum] = sorted(PriorityEnum, key=lambda x: x.value, reverse=True)
