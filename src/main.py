from src.contracts.task_source import TaskSource
from src.sources.task_json import TaskSourceJSON
from src.sources.task_gen import TaskSourceGen
from src.sources.task_api import TaskSourceAPI
from src.task_queue.task_queue import TaskQueue
from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum


def main() -> None:
    """
    Функция вызывает источники задач через единный контракт
    для добавления новых необходимо импортировать их и добавить в source_list
    :return: Данная функция ничего не возвращает
    """
    source_list: list[TaskSource] = [TaskSourceJSON("example.jsonl"), TaskSourceGen(), TaskSourceAPI()]

    queue = TaskQueue()
    for source in source_list:
        if not isinstance(source, TaskSource):
            print(f"bad task source {source.__class__.__name__}")
            continue

        print(f"collecting tasks from {source.__class__.__name__}")
        queue.add_task(source.get_tasks())
        print(f"queue size: {len(queue)}")
        for i, task in enumerate(queue):
            if i >= 3:
                break
            print(f"do task id: {task.id}\n\tpriority: {task.priority.name}\n\tstatus: {task.status.value}\n\ttime of creation: {task.creation_time}")
            print("\t" + str(task.payload))
        print()

    print("filter by status SCHEDULED")
    for task in queue.filter_by_status(StatusEnum.SCHEDULED):
        print(f"do task id: {task.id}\n\tpriority: {task.priority.name}\n\tstatus: {task.status.value}")
        print("\t" + str(task.payload))
    print()

    print("filter by priority >= HIGH")
    for task in queue.filter_by_priority(PriorityEnum.HIGH):
        print(f"do task id: {task.id}\n\tpriority: {task.priority.name}\n\tstatus: {task.status.value}")
        print("\t" + str(task.payload))
    print()


if __name__ == "__main__":
    main()
