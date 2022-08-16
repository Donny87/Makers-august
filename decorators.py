""" Декораторы - это функция которая расширяет функционал другой функции не изменяя ее кодовой базы 

Функция высшего порядка - принимает в качестве аргумента другую функцию или возвращает объект в качестве  функции """

# def func1():
#     print('I am fuction1 ')

# def func2():
#     func1()
#     print('I am fuction2 ')

# func1()
# func2()


# def func():
#     print('i am func!!!')

# def func2(func):
#     func()
#     print('i am func2!!!')

# func2(func = func)    # i am func!!!
# #i am func2!!!

# def func1():

#     def func2():
#         print('i am func2!!!')
#     print(' am fuction1') 
#     func2()   

# func1()

# def func1():

#     def func2():
#         return ('i am func2!!!')
#     print(' am fuction1') 
#     return func2   

# func = func1()

# print(func())



# def decorator(func):
#     def wrapper():
#         print('I runing before main func')
#         func()
#         print('I runing after main func')

#     return wrapper

# def main():
#     print('I am main fuction')    

# decorator_main = decorator(main)    
# decorator_main()

# I runing before main func
# I am main fuction
# I runing after main func




# def decorator(func):
#     def wrapper():
#         print('I runing before main func')
#         func()
#         print('I runing after main func')

#     return wrapper

# @decorator - синтаксический сахар
# def main():
#     print('I am main fuction')    
# main()    

# I runing before main func
# I am main fuction
# I runing after main func


# def decorator_count(func):
#     def wrapper(name, last_name):
#         print('Добро пожаловать !')
#         func(name, last_name)
#         print('Количество участников: 12')

#     return wrapper
# @decorator_count
# def main(name: str, last_name: str):
#     print(f'{name.capitalize()} {last_name.capitalize()}')

# main('python', 'dor')

# Добро пожаловать !
# Python Dor
# Количество участников: 12



# def bread(function):
#     def wrapper():
#         print('bread')

#         function()
#         print('bread')
#     return wrapper    

# def salad(function):
#     def wrapper():
#         print('salat')
#         function()
#         print('salat')
#     return wrapper    

# @bread
# @salad
# def func():
#     print('Котлета')    

# func()    

# bread
# salat
# Котлета
# salat
# bread


# from datetime import datetime

# def time_check(func):
#     def wrapper(*args, **kwargs):
#         start_time = datetime.now()
#         func(*args, **kwargs)
#         end_time = datetime.now()
#         print('время выполнения')
#         print(end_time - start_time)
#     return wrapper  

# @time_check
# def generate_range(*args, **kwargs):
#     for i in range(args[0]):
#         print(pow(args[1], 23))

# generate_range(99, 122423423)


# время выполнения
# 0:00:00.001718


def somefunc():
    print('hello Dastan')

def decorator(somefun)    


# def decorator(func):
#     def wrapper(*donny, ** ddd):
#         print('some shit')
#         print(donny)
#         # func(donny)

#     return wrapper        
# @decorator
# def somefunc(a,b):
#     print('hello Atai')

# somefunc(5,10)    