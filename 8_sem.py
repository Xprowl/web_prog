# f = open('text.txt', 'a')
# # print(f.read())
# # for line in f:
# #     print(line)
# for line in f:
#     print(line.write(line + "123"))

# Перезапись 
# l = [str(i)+str(i-1) for i in range (20)]
# print (l)
# f = open('test.txt', 'a')
# for index in l:
#     f.write(index+'\n')
# f.close()

# l = [str(i)+str(i-1) for i in range (20)]
# print (l)
# f = open('test.txt', 'a')
# for index in l:
#     f.write(index+'\n')
# f.close()

# f = open('test.txt', 'r')

# for line in f:
#     print(l)
# f.close()

# l = ["first\n", "second\n", "third\n", "fourth\n"]
# with open("example.txt", 'w') as file:
#     for line in l:
#         file.write(line)

# f = open('example.txt', 'a')
# # print(f.read())
# # for line in f:
# #     print(line)
# for line in f:
#     print(line.write(line + "123"))


# Задача один копирование файла, создание нового
# with open("example.txt", "r") as f:
#     content = f.read()
# with open ("copy.txt", "w") as f:
#     f.write(content)
# print("Скопировано")

# f = open('text.txt', 'r')
# print(f.read())
# for line in f:
#     print(line)


# Списки картежи словари множества, соотвесенно каждая имеет свои особенности и применяется в разилчных ситуациях.
# 1) тип списки в пайтон это изменяемых которые могут содержать элементы разных типов [] является чаще всего используемым в пайтоне. 
# empty_list = []

# numbers = [1,2,3,5,4,6]
# numbers2 = [8,9,10]
# fruits = ["apple", "banana", "orange"]

# numbers.sort()

# print(numbers)

#2) Картежи в пайтон очень важно понять концепцию, это не изменяемая последовательность действий

# numbers_tuple = (1,2,3,4,5)

# for tup in numbers_tuple:
#     tup = 1
# print(numbers_tuple)

# 3) Словари в патане хранят ключи, они уникальные и не изменные, а значение могут разными могут быть, создание словарей точно также, выполняется через скобки но чрезе фигурные скобки

# persons = {"person_1":{"name": "Max", "age": 27, "city": "Krasnodar"}, "person_2":{"name": "Alex", "age": 25, "city": "Krasnodar"}}

# print (persons ["person_1"])

# 4) Множество в пайтен это коллекция создаются с помощью фигурных у них не присваиваются ключи, у них элементы не упорядочены.

# empty_set = set()

# numbers_set = {1,2,3,4,5}

# fruit = {"apple", "mango", "orange", 4}

# test = numbers_set.intersection(fruit)
# print(test)


# Задача 1

# persons = {"person_1":{"name": "Tom", "age": 39, "Company": "SuperCorp", "Programming": ["Pythone", "JavaScript"]}}

# print (persons ["person_1"])

# Задача 2

# Пусть дан следующий список, которые хранит несколько словарей:

# people = [
#     {"person_1"{"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]}},
#     {"person_2"{"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]}},
#     {"person_3"{"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}}
# ]

# # Каждый словарь в списке представляет программиста, где поле "name" представляет имя,
# #  а поле "languages" - список используемых языков программирования. 
# # Выведите на консоль из каждого словаря имя и последний язык программирования, чтобы получился следуюший консольный вывод:

# # Name:  Tom
# # Last language:  JavaScript
# # Name:  Bob
# # Last language:  C#
# # Name:  Sam
# # Last language:  Java

# print (people ["person_1"])
