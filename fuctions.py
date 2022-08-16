""" функции """

# print()
# max()
# pow()

# функция - именнованый блок кода , который принимает какие-либо значения, 
# совершает какие-то действия над ними и возвращает результат этих действий.

# a1 = 100
# (a1 ** 2) / 10 * 15
# a2 = 200
# (a2 ** 2) / 10 * 15
# a3 = 200
# (a3 ** 2) / 10 * 15


# DRY(Don't repeat yourself) - не повторяйся


# def func():
#     print('Hello world')

# func()    -   Hello world

# def my_sqr(num):
#     print((num ** 2) / 10 * 15)

# my_sqr(100)   # - #15000.0
# my_sqr(300)   # - 135000.0


# b = my_func(100) # - 15000.0
# def my_func(num):
#     return (num ** 2) / 10 * 15
# print(b)
# print(b + 500)

# def func():
#     return None

""" def имя_фунции(параметры):
                тело_фунции        

имя_функции(аргументы)

параметры - это значения функции при объявлении
аргументы - это значения для функции при вызове
return - ключевое слово для возвращения результата выполнения фунции            """
              


# def add(x: int, y: int) -> int:
#     """ принимает 2 числа и складывает их между собой """ # строка документации (docstring)
#     num = x + y
#     return num

# print(add(40, 70)) # - 110    


# 1. Обязательные (c)
# 2. Необязательные (c=10)

# def sub(x, y):
#     res = x - y
#     return res

# a = sub(10, 25)    # 15

# def sub1(x, y=5):
#     res = x - y
#     return res

# b = sub1(10)        # 5
# с = sub1(50, 10)    # 40

# def func(x=5, y): # SyntaxError

# def func(a, b, c, d, e=10, f=20):
#     pass


# аргументы бывают двух типов:
# 1. именнованные
# 2. позиционные

# def my_func(num1, num2, num3 = 10):
#     return num1 + num2 + num3

# позиционные
# my_func(10, 25, 30)     # 65
# my_func(50, 60) # 120

# именнованные
# my_func(num1=5, num2=10, num3=15)
# my_func(num2=10, num3=15, num1=5)

# my_func(10, 5, num3=10) # 25
# my_func(num3=5, 5, 10) # Error
# my_func(10, 5, num1=15) # Error





# def send_message(email, message):
#     return f'{message} было отправленно на {email}'

# def notify_user(name):
#     message = input('Введите сообщение')
#     email = input('Введите почту')
#     note = send_message(email, message)
#     print(f'Здравствуйте {name}. {note}')    

# notify_user('Актан')    


# *args - кортеж позиционных аргументов (arguments)
# **kwargs - словарь именнованных аргументов (keyword arguments


# def func(*args, **kwargs):
#     print(args, 'args')
#     print(kwargs, 'kwargs')

# func(1, 2, 3, 4)    # args -> (1,2,3,4)
# func(a=1, c=3, d=55) # kwargs -> {'a': 1, 'c': 3, 'd': 55}
# func(1, 2, 3, 4 a=10, b=20, c=30)

# def my_func(*args):
#     counter = 0
#     for i in args:
#         try:
#             counter += i
#         except TypeError:
#             print(f'{i} не является числом')
#     return counter


# print(my_func(1, 2, 3, 4, 'fghjk', 6))