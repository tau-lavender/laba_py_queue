import json
from typing import Iterable
from src.contracts.task import Task
from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum


class TaskSourceJSON:
    """
    Источник задач - из JSON файла
    """

    def __init__(self, filename: str) -> None:
        if not filename.endswith(".jsonl"):
            raise NameError(f"{filename} is not json")
        self.filename = filename

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач соответствующий протоколу TaskSource
        """

        with open(self.filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                raw = json.loads(line)
                payload = raw.get("payload", "")
                if payload == "":
                    raise ValueError("No payload in json {filename}, line {line_no}")
                priority = raw.get("priority", "")
                if priority in [en.name for en in PriorityEnum]:
                    enum_priority = PriorityEnum[priority]
                status = raw.get("status", "")
                if status in [en.name for en in StatusEnum]:
                    enum_status = StatusEnum[status]
                if priority == "" and status == "":
                    yield Task(payload)
                if priority != "" and status == "":
                    yield Task(payload, priority=enum_priority)
                if priority == "" and status != "":
                    yield Task(payload, status=enum_status)
                if priority != "" and status != "":
                    yield Task(payload, priority=enum_priority, status=enum_status)
