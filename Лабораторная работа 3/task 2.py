def find_common_participants(gr1, gr2, separator=','):
    """
    Находит общих участников в двух группах.

    Аргументы:
        group1: строка с участниками первой группы
        group2: строка с участниками второй группы
        separator: разделитель между фамилиями (по умолчанию ',')

    Возвращает:
        список общих участников, отсортированный по алфавиту
    """
    # Метод split() разделяет строку на список по указанному разделителю
    list1 = gr1.split(separator)
    list2 = gr2.split(separator)

    # Преобразуем списки в множества для использования метода intersection()
    set1 = set(list1)
    set2 = set(list2)

    # Метод intersection() возвращает множество общих элементов
    common_set = set1.intersection(set2)

    # Сортируем результат и возвращаем список
    return sorted(common_set)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызываем функцию с разделителем '|'
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    '|'
)

print("Общие участники:", common_participants)