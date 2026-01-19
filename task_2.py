# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    """
    Функция для поиска общих участников двух групп.

    Аргументы:
    group1 -- строка с участниками первой группы
    group2 -- строка с участниками второй группы
    separator -- разделитель (по умолчанию запятая)

    Возвращает:
    Список общих участников, отсортированный в алфавитном порядке
    """
    # Разделяем строки на списки участников
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Находим общих участников с помощью множеств
    common_participants = set(participants1) & set(participants2)

    # Преобразуем в список и сортируем
    result = sorted(list(common_participants))

    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"