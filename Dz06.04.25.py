# Задание 1

# def longest_words(file):
#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             text = f.read()  # читаем весь текст из файла
#             words = text.split()  # разбиваем на слова
#             max_len = max(len(word) for word in words)  # находим максимальную длину слова
#             longest = [word for word in words if len(word) == max_len]  # собираем все слова с максимальной длиной
#             print("Самые длинные слова:", longest)
#     except FileNotFoundError:
#         print(f"Файл '{file}' не найден.")
# longest_words("article.txt")

# with open(file, 'r', encoding='utf-8') as f: — открываем файл для чтения.

# text = f.read() — читаем всё содержимое файла в одну строку.

# words = text.split() — разбиваем текст на отдельные слова (по пробелам и переводам строк).

# max(len(word) for word in words) — определяем максимальную длину слова.

# [word for word in words if len(word) == max_len] — ищем все слова, длина которых равна максимальной.

# print(...) — выводим результат.

# except FileNotFoundError — обработка случая, если файл не найден.
# Задание 2
# def calculate_total_price(file):
#     total = 0 (Начальная сумма в начале 0)
#     try: (Начало блока обработки исключений — если файл не будет найден, программа не завершится с ошибкой, а выведет сообщение.)
#         with open(file, "r", encoding="utf-8") as f:
#             for line in f: (Цикл for — проходит построчно по всему содержимому файла.)
#                 parts = line.strip().split('\t')  # Разделяем по табуляции
#                 if len(parts) == 3: Проверка, что в строке действительно три элемента (на случай ошибок в файле).
#                     name, quantity, price = parts
#                     total += int(quantity) * int(price) вычисления
#         print(f"Общая стоимость заказа: {total} рублей")
#     except FileNotFoundError:
#         print(f"Файл '{file}' не найден.")


# Читает файл построчно.
# Разделяет строку по \t.
# Преобразует количество и цену в int, считает сумму.
# Выводит итог.

# line.strip() — убирает пробелы и символы новой строки с начала и конца строки. 
# split('\t') — разделяет строку по символу табуляции \t, возвращая список из трёх элементов:

# Задание 3

# def read_csv():
#     result = []
#     with open('data.csv', encoding='utf-8') as f:
#         # Считываем строки
#         lines = f.readlines()
#         # Получаем заголовки из первой строки
#         keys = lines[0].strip().split(',')
#         # Обрабатываем каждую оставшуюся строку
#         for line in lines[1:]:
#             values = line.strip().split(',')
#             # Формируем словарь и добавляем в результат
#             row_dict = dict(zip(keys, values))
#             result.append(row_dict)
#     return result

# Задание 4

# with open('file.txt') as f:
# 	txt = f.read()
# 	print('Input file contains:')
# 	print(sum(map(str.isalpha, txt)), 'letters')
# 	print(len(txt.split()), 'words')
# 	print(txt.count('\n') + 1, 'lines')