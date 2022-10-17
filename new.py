import os
clear = lambda: os.system('cls')
clear()
# a = int(input('Введите а: '))
# while a !=5:
#     a = int(input('Непойдёт, давай ещё а: '))
# b = int(input('Введите b: '))
# if b > 10:
#     print('Эй! ну куда?')
# c = a + b
# print('{} + {} = {}'.format(a, b, c))
# text = 'ffffffffffffffffff'
# print(text.replace('f','A'))

# n= 2658
# while n > 1440:
#     n -=1440
# h = n//60
# m = n%60
# print(h, m)

# n = int(input())
# sec=n%60
# min=n//60%60
# h=n//60//60%24
# print(f'{h}:{min if (min//10)>0 else str(0)+str(min)}:{sec if (sec//10)>0 else str(0)+str(sec)}')

# a = int(input())
# b = int(input())
# a,b=b,a
# print(a, b)

# a = int(input())
# a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
# print(a//60 + 9, a%60)

# Задача 5
# a = int(input())
# b = int(input())
# n = int(input())
# rub = int(a*n)
# cop = int(b*n)
# while cop > 99:
#     rub += 1
#     cop -= 100
# print(rub, cop)

# Задача 6
# h1 = int(input())*3600
# m1 = int(input())*60
# s1 = int(input())
# h2 = int(input())*3600
# m2 = int(input())*60
# s2 = int(input())
# print((h2 + m2 + s2)-(h1 + m1 + s1))

# Задача 7
# kmS = int(input())
# km = int(input())

# print(-1 * km // kmS * -1)

# Задача 8
# year = int(input())
# print('YES' if ((year%4)==0 and (year%100)!=0) or (year%400)==0 else 'NO')


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# x = input('Введите число: ')

# def summa(x):                            #Функция нахождения суммы чисел в заданном числе
#     if float(x) < 0:                            #Проверка на знак перед числом
#         x = float(x) * (-1)
#     number = 0

#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number

# print(f'Сумма чисел равна: {summa(x)}')


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число: '))

# f = 1
# for i in range(N):
#     i +=1
#     f = i * f
#     print(f, end=" ")


# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

# n = int(input('Введите количество чисел в списке: '))

# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1}: '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ

# print('Сумма чисел равна:',round((numbers(n)), 2))


# _____________________________________DZ3________________________________________________

# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# x = [2, 3, 6, 10, 12, 16, 5]
# summ = 0
# for i in range(1, len(x), 2):
#     #if i % 2 == 1:
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# list = [2, 3, 6, 4, 3, 5]
# import math 
# size = math.ceil(len(list)/2)
# print(size)
# list2 = []
# for i in range(size):
#     list2.append(list[i]*list[-i - 1])
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# x = [1.1, 1.2, 3.1, 5, 10.01]
# x1 = []
# for i in range(len(x)):
#     if x[i] % 1 != 0:
#         x1.append(x[i])
# x2 = [round(x1[i] % 1, 2) for i in range(len(x1))]
# print(f"{x2} => {max(x2) - min(x2)}")

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# x = int(input("Введите число:  "))
# print(bin(x)[2:])

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))