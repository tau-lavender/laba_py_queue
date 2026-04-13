from src.contracts.task_source import TaskSource
from src.sources.task_json import TaskSourceJSON
from src.sources.task_gen import TaskSourceGen
from src.sources.task_api import TaskSourceAPI


def main() -> None:
    """
    Функция вызывает источники задач через единный контракт
    для добавления новых необходимо импортировать их и добавить в source_list
    :return: Данная функция ничего не возвращает
    """
    source_list: list[TaskSource] = [TaskSourceJSON("example.jsonl"), TaskSourceGen(), TaskSourceAPI()]
    for source in source_list:
        if not isinstance(source, TaskSource):
            print(f"bad task source {source.__class__.__name__}")
            continue

        print(f"collecting tasks from {source.__class__.__name__}")
        for task in source.get_tasks():
            print(f"do task id: {task.id}\n\tpriority: {task.priority.name}\n\tstatus: {task.status.value}\n\ttime of creation: {task.creation_time}")
            if not isinstance(task.payload, str):
                raise TypeError(f"{task.payload} not string")
            print("\t" + task.payload)
        print()


if __name__ == "__main__":
    main()
