#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_task(**kwargs):
    tasks.append(kwargs)


if __name__ == "__main__":
    tasks = []

    add_task(title="Изучить Python", status="в процессе", priority="высокий")
    add_task(title="Закончить проект", status="не начато", deadline="30.11.2023")
    add_task(title="Подготовить презентацию", status="завершено", date="15.12.2023")

    print("Список задач:")
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task}")
