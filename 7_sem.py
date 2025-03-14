# Рекурсия Метод внутри своего тела вызывает самого себя fact(n-1)
# Стоится по двух условия выхода из рекурсии,
# LIFO обработки очереди какой либо в программных средах, last input first out, стек это хранилище внутри стека. Если мы не указываем, будет переполнение памяти.
# Условием выхода будет парамет который является параментром на поставленую задачу, смотрим на факториал, пока не достигунут до еденицы, если наше число больше 1, ifn>1
# fact(n-1)*n
# else:
# return 1

# def fact (n):
#     if n>1:
#         return fact(n-1)*n
#     else:
#         return 1

# print (fact(5))

# Напишите программу которая будет принимать на вход число а на выходе показывать сумму цифр этого числа.

# def sum_fact(num):
#     if num <= 0:
#         return 0
#     else:
#         return sum_fact(num//10) + num % 10

# print(sum_fact(123456789))

# Напишите программу которая выведет все натуральные числа в промежутке от 1 до N
# 5 = 1 2 3 4 5 

# def r_num(num):
#     if num <= 0:
#         return 0
#     else:
#         r_num(num-1)
#         print(num, end=" ")

# r_num(10)


# Считать ставку из консоли содержащие латинские буквы.
# Вывести на экран все согласные буквы этой строки.
# hello => h i l

# ALPHA = ["ayeoiu"]

# def find_let(string_found):
#     if len(string_found)<= 0:
#         return
#     else:
#         if string_found[-1] not in ALPHA:
#             print(string_found[0], end="")
#         find_let(string_found[1:])

# find_let("Hello")
