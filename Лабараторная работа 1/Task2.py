# TODO Найдите количество книг, которое можно разместить на дискете
# Параметры дискеты
disk_MB = 1.44  # Мб
disk_bytes = disk_MB * 1024 * 1024  # перевод в байты
# Параметры книги
pages = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4
# Объем книги в байтах
book_bytes = pages * lines_per_page * symbols_per_line * bytes_per_symbol
# Количество книг, которое поместится
# Используем целочисленное деление, так как книги неделимы
# Вводим через int
n = int(disk_bytes // book_bytes)
print("Количество книг, помещающихся на дискету:", n)
