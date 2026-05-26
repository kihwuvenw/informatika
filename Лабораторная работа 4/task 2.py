import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file_csv:
        # Используем csv.DictReader для автоматического преобразования в словари
        # Первая строка CSV будет использована как ключи
        reader_csv = csv.DictReader(file_csv)

        # Преобразуем все строки в список словарей
        result_data = list(reader_csv)

    # Сериализуем в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file_json:
        json.dump(result_data, file_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Выводим содержимое output.json для проверки
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_file:
        for single_line in output_file:
            print(single_line, end="")

