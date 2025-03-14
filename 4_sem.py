# def test(a,b):
#     return (a+b)

# print(test(3,5))

# Задача 1

# Напишите функцию sum_range(start, end), 
# которая суммирует все целые числа от значения start до величины end включительно. 
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

# def sum_range(start, end):
#     if (start > end):
#         start, end = end, start
#     sum = 0
#     while(end>=start):
#         sum+=start
#         start+= 1
#     print(sum)
# sum_range(1,-5)

# Задача 2

# Написать функцию season, принимающую 1 аргумент — 
# номер месяца (от 1 до 12), и возвращающую время года, 
# которому этот месяц принадлежит (зима, весна, лето или осень).

# def season(month):
#     if month in (12, 1, 2):
#         return "зима"
#     elif month in (3, 4, 5):
#         return "весна"
#     elif month in (6, 7, 8):
#         return "лето"
#     elif month in (9, 10, 11):
#         return "осень"
#     else: return "Такого месяца не существует!"
        
# print (season(int (input ("Введите номер месяца"))))

# Задача 3

# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

# def sqrt(number):
#     return int(number**0.5)

# def is_prime(num):
#     if num in (0,1,2):
#         return True
#     else:
#         if num %2 == 0:
#             return False
#         else:
#             for i in range(3,sqrt(num)+1, 2):
#                 if num % i == 0:
#                     return False
#             else: 
#                 return True
        
# print(is_prime(int(input("Введите число от 0 до 1000: "))))



# import random

# def get_random_array(size, crit):
#     arr = random.choices(range(crit), k=size)
#     return arr

# def sqrt(number):
#     return int(number**0.5)

# def is_prime(num):
#     if num in (0,1,2,3):
#         return True
#     else:
#         if num % 2 == 0:
#             return False
#         else:
#             for i in range(2, sqrt(num)+1, 2):
#                 if num % i == 0:
#                     return False
#                 else: 
#                     return True
                
# arr = get_random_array(10,10)
# print(arr)
# sum = 0
# for i in arr:
#     flag = bool(is_prime(i))
#     if flag==True:
#         sum+=1
# print ("Кол-во простых чисел в массиве: ", sum)

# import random

# def get_random_array(size, crit):
#     arr = random.choices(range(crit), k=size)
#     return arr
                
# arr = get_random_array(10,10)
# print(arr)
# for i in range(len(arr)):
#     arr[i] *= -1
# print(arr)