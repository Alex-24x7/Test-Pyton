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