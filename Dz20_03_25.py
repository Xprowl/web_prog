# Строки 
# Задание1
# Двумерный массив символов → строка
# char = [['a', 'b', 'c'], ['d', 'e', 'f']]
# result = ''.join(''.join(row) for row in char)
# print(result)
# Задание2
# Замена заглавных букв на строчные
# text = "aBcD1ef!-"
# result = text.lower()
# print(result)
# Задание3
# Проверка на палиндром
# def palindrome(s):
#     return s == s[::-1]
# print(palindrome("aBcD1ef!-"))
# print(palindrome("шалаш"))
# print(palindrome("55655"))
#Рекурсия
#Задача 1: Вывести числа от M до N рекурсией
# def print_range(m, n):
#     if m > n:
#         return
#     print(m, end=", " if m < n else "\n")
#     print_range(m + 1, n)

# print_range(1, 5)
# print_range(4, 8)
# Задача 2: Функция Аккермана
# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return ackermann(m - 1, 1)
#     else:
#         return ackermann(m - 1, ackermann(m, n - 1))

# print(ackermann(2, 3))  # 29
# Задача 3: Рекурсивный вывод массива в обратном порядке
# def print_reverse(arr, i=0):
#     if i == len(arr):
#         return
#     print_reverse(arr, i + 1)
#     print(arr[i], end=" ")

# arr = [1, 2, 5, 0, 10, 34]
# print_reverse(arr)