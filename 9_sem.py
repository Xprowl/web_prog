# Напишите функцию tpl_sort(), которая сортирует кортеж, состоит и целых чисел по возрастанию,
# и возвращает его. Если хотя бы один элемент не является целым числом, вернуть кортеж в 
# изначальном виде

# def tpl_sort(tpl):
#     for c in tpl:
#         if c%1 > 0:
#             return tpl
#     return tuple(sorted(tpl))
# tpl = (1,3.125,2,4,5)
# print(tpl_sort(tpl))

# Функция slicer() на вход принимает кортеж и случайный элемент. 
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента 
# в нем и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, 
# который начинается с него и идет до конца исходного.

# def slicer(tpl, elem):
#     if elem in tpl:
#         if tpl.count(elem) > 1:
#             first = tpl.index(elem)
#             second = tpl.index(elem, first+1)+1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(elem):]
#     else:
#         return ()
# tpl = (1,3.125,2,4,5,2)
# print(slicer(tpl,11))

# Дан словарь {'class':{'student':{'name':'Mike','marks':{'physics':70,'history':80}}}}. 
# Выведите на экран имя студента и его оценку по истории

# test = {'class':[{'student':{'name':'Mike','marks':{'physics':70,'history':80}}},
#                 {'student':{'name':'Max','marks':{'physics':30,'history':90}}},
#                 {'student':{'name':'Lake','marks':{'physics':11,'history':50}}}]
#         }

# for student in test['class']:
#     print("Имя студента: ", student['student']['name'])
#     for (name, mark) in student['student']['marks'].items():
#         print("Оценка по" , name, ":", mark)
#     print()