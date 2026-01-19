# TODO решите задачу
import json


def task() -> float:
    """Функция для вычисления суммы произведений score * weight из JSON файла."""
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Используем генератор для вычисления суммы
    total = sum(item['score'] * item['weight'] for item in data)

    return round(total, 3)


print(task())