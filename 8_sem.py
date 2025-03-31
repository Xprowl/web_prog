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
