from typing import Optional, Iterable, Iterator

from src.contracts.task import Task
from src.enums.priority_enum import PriorityEnum, PRIORITY_ENUM_ORDER
from src.enums.status_enum import StatusEnum


class TaskQueue:
    """
    Очередь для задач из источников
    """

    def __init__(self, tasks: Optional[Iterable[Task]] = None) -> None:
        self._queues: dict[PriorityEnum, list[Task]] = {
            x: [] for x in PRIORITY_ENUM_ORDER
        }
        self._index: int = 0
        self._full_list: list[Task] = []

        if tasks:
            for task in tasks:
                self.add_task(task)

    def _upd_full_list(self):
        self._full_list = []
        for priority in PRIORITY_ENUM_ORDER:
            self._full_list.extend(self._queues[priority])

    def add_task(self, tasks: Task | list[Task]) -> None:
        if isinstance(tasks, Task):
            task_to_add = [tasks]
        elif isinstance(tasks, Iterable):
            task_to_add = list(tasks)
            for task in task_to_add:
                if not isinstance(task, Task):
                    raise TypeError(f"{id} not Task")
        else:
            raise TypeError(f"{tasks} is not int or iterable")

        for task in task_to_add:
            self._queues[task.priority].append(task)
        self._upd_full_list()

    def remove_task(self, task_ids: int | Iterable[int]) -> None:
        if isinstance(task_ids, int):
            id_to_remove = {task_ids}
        elif isinstance(task_ids, Iterable):
            id_to_remove = set(task_ids)
            for id in id_to_remove:
                if not isinstance(id, int):
                    raise TypeError(f"{id} not int")
        else:
            raise TypeError(f"{task_ids} is not int or iterable")

        for priority in PRIORITY_ENUM_ORDER:
            queue = self._queues[priority]
            to_del = []
            for i, task in enumerate(queue):
                if task.id in id_to_remove:
                    to_del.append(i)

            for i in reversed(to_del):
                del queue[i]

        self._upd_full_list()

    def filter_by_status(self, status: StatusEnum) -> Iterator[Task]:
        for priority in PRIORITY_ENUM_ORDER:
            for task in self._queues[priority]:
                if task.status == status:
                    yield task

    def filter_by_priority(self, priority: PriorityEnum) -> Iterator[Task]:
        for task in self._queues[priority]:
            yield task

    def __getitem__(self, index: int) -> Task:
        return self._full_list[index]

    def __delitem__(self, index: int) -> None:
        task_to_delete = self._full_list[index]
        self.remove_task(task_to_delete.id)

    def __len__(self) -> int:
        return len(self._full_list)

    def __iter__(self) -> 'TaskQueue':
        self._index = 0
        return self

    def __next__(self) -> Task:
        if self._index >= len(self._full_list):
            raise StopIteration
        task = self._full_list[self._index]
        self._index += 1
        return task

    def __repr__(self) -> str:
        return f"{self._full_list}, len: {len(self._full_list)}"
