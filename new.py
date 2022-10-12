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


