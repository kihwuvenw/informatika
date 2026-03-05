numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Находим индекс пропущенного элемента (None)
index_of_none = numbers.index(None)
# Считаем сумму всех чисел, кроме None
total_sum = sum(x for x in numbers if x is not None)
# Количество элементов в списке
count = len(numbers)
# Среднее арифметическое (оно будет дробным, даже если сумма целая)
average = total_sum / count
# Заменяем None на среднее арифметическое
numbers[index_of_none] = average
# Выводим
print("Измененный список:", numbers)

