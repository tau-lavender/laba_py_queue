import pytest  # type: ignore
from datetime import datetime

from src.main import main
from src.contracts.task import Task
from src.contracts.task_source import TaskSource
from src.sources.task_json import TaskSourceJSON
from src.sources.task_gen import TaskSourceGen
from src.sources.task_api import TaskSourceAPI
from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum


class TestMain:
    def test_main(self):
        main()


class TestTask:
    def test_task_init(self):
        payload = "ababa"
        task = Task(payload=payload)
        assert task.payload == payload
        assert isinstance(task.creation_time, datetime)
        assert task.priority == PriorityEnum.NORMAL
        assert task.status == StatusEnum.SCHEDULED


class TestTaskSource:
    def test_duck_typing(self):
        a = TaskSourceJSON("example.jsonl")
        b = TaskSourceGen()
        c = TaskSourceAPI()
        assert isinstance(a, TaskSource)
        assert isinstance(b, TaskSource)
        assert isinstance(c, TaskSource)
        assert all([isinstance(x, Task) for x in a.get_tasks()])
        assert all([isinstance(x, Task) for x in b.get_tasks()])
        assert all([isinstance(x, Task) for x in c.get_tasks()])

    def test_bad_duck_typing(self):
        class Ababa:
            ...
        a = Ababa()
        assert not isinstance(a, TaskSource)


class TestTaskSourceJSON:
    def test_not_json(self):
        with pytest.raises(NameError):
            TaskSourceJSON("tests/not_json.txt")

    def test_bad_json(self):
        with pytest.raises(ValueError):
            for task in TaskSourceJSON("tests/bad_json.jsonl").get_tasks():
                assert isinstance(task, Task)
