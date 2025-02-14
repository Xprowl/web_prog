#Напишите программу, которая на вход принимает два числа, а на выходе, отдает какое число больше, а какое меньше


#firsth_numb = int(input('Enter first numb: '))
#second_numb = int(input('Enter second numb: '))

#if firsth_numb > second_numb:
#    print(firsth_numb, 'greater_than', second_numb)
#else:
#    print(second_numb, 'greater_than', second_numb)

#print(firsth_numb,second_numb)

#Напишите программу которая принимает 3 числа и выдаёт максимальное из них5

#firsth_numb = int(input('Enter first numb: '))
#second_numb = int(input('Enter second numb: '))
#third_numb = int(input('Enter third_numb: '))

#max = firsth_numb

#if max < second_numb and second_numb > third_numb:
#    max = second_numb
#elif max < third_numb and third_numb > second_numb:
#    max = second_numb
#else:
#    max = max
#
#print("Max numb is - ", max)

#Напишете программу, которая прнимает на вход два числа и выдаёт какое из них четное а какое нечетное (в случае одинаковой четности вывести оба числа)

#first_numb = int(input('Enter first numb: '))
#second_numb = int(input('Enter second numb: '))

#if first_numb%2 == 0 and second_numb%2:
#    print(first_numb,second_numb," - even")
#elif second_numb%2 ==0:
#    print(second_numb, " - even")
#elif first_numb%2 == 0:
#    print(first_numb, " - even")
#else:
#    print("no even numbers")


#Напишите программу, которая на вход принимает число, а на выходе показывает все четные исла от 1 до этого числа 
#numb = int(input("Enter your number: "))
#
#for i in range(1, numb+1):
#    if i%2 == 0:
#        print(i,end=' ')


# Домашнее задание

# a = int(input("Введите число: "))
# print("да" if a % 7 == 0 and a % 23 == 0 else "нет")

#x, y = map(int, input("Введите координаты X и Y: ").split())

#if x > 0 and y > 0:
#    print(1)
#elif x < 0 and y > 0:
#    print(2)
#elif x < 0 and y < 0:
#    print(3)
#else:
#    print(4)