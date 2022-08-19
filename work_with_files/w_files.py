""" Работа с файлам """

# Операции над файлами: 
# 1. Чтение файлов
# 2. Запись

# Файлы бывают текстовыми и бинарными

# open(путь_до_файла, режим работы) - функция для открытия файлов

# file = open('test.txt', 'r')
# print(file.read()) # work with files
# file.close()


"""
r -  чтение 
w - записи, создает файл, перезаписывает соддержимое файла, если такой файл существует
x - запись, если файла не существует, иначе исключение
a - дозапись 
w+, r+ - запись и чтение 
b - открытие бинарных файлов
t - открытие текстовых файлов
rt - режим по умолчанию
"""


# file = open('test.txt', 'r')
# print(file.read(5)) 
# file.close()

# read() - читает весь файл или n символом, если указан

# file1 = open('test.txt')
# for row in file1:
#     print(row)
# file.close()    


# file2 = open('test.txt')
# words = file2.readlines()
# list_ = []
# for word in words:
#     list_.append(word.strip())
# print(list_)    # ['work', 'with', 'makers', 'world', 'donny']

# file2.close() # ['work\n', 'with\n', 'makers\n', 'world\n', 'donny']


# readlines()- читает файл и возвращает список из строк


# image = open('bridge.jpg', 'rb')
# print(image.read())
# image.close()


# file4 = open('test2.txt')
# print(file4.read())
# file4.seek(0)
# print(file4.read())
# print(file4.tell())
# file4.close()

# seek(n) - перенос курсора на n позицию
# tell() - cообщает положение курсора


# with open('test2.txt', 'r') as file10:
#     print(file10.read())

# try:
#     file10.read()
#     file10.seek(0)
# finally:
#     file10.close()        



# with функция() as название: - контекстный менеджер
#     тело_менеджера


# with open('test2.txt', 'r') as file1:
#     print(file1.readlines())

# file1.read()    



# with open('test3.txt', 'w') as f:
#     f.write('apple\n')
#     f.write('watermelon\n')
#     f.write('potato\n')
#     f.write('snickers')





# with open('test4.txt', 'w+') as f:
#     list_ = ['makers', 'fuckers', 'girls', 'cars']
#     n = [name + "\n" for name in list_]
#     f.writelines(n)
#     f.seek(0)
#     print(f.read())


# with open('prog.txt', 'w+') as f:
#     f.write('for i in range(1, 10):\n\tprint(i)')
#     f.seek(0)
#     code = f.read()
#     exec(code)
    