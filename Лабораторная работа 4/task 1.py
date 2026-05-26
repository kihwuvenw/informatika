import json


def task() -> float:
    # Читаем JSON файл (предполагается, что файл называется 'data.json')
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Вычисляем сумму произведений score * weight
    answer = sum(item['score'] * item['weight'] for item in data)

    # Округляем до 3 знаков и возвращаем
    return round(answer, 3)


if __name__ == "__main__":
    print(task())
