import os
clear = lambda: os.system('cls')
clear()

with open('hello.txt', 'a', encoding='utf-8') as data:
    data.write('\nНовая строка 1')
    data.write('\nНовая строка 2')


# file_1 = open('hello.txt', 'a', encoding='utf-8')
# colors = '\nДописываем инфу'
# file_1.writelines(colors)
# file_1.close()

with open('hello.txt', 'r', encoding='utf-8') as data:
    print(data.read())

# file_2 = open('hello.txt', 'r', encoding='utf-8')
# content = file_2.read()
# print(content)
# file_2.close()