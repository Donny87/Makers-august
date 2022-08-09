""" try except """
# try except - конструкция для обработки исключений

# исключение - проблема в логике работы кода 
# ZeroDivisionError - ошибка деления на ноль
# print(10 / 0)


# NameError: - исключение отсутствия имени
# a = 10
# b = 20
# print(c)


# AtributeError: - ошибка атрибута
# string  = 'word'
# string.get('o')


# KeyError: - ошибка ключа
# dict_ ={'a': 10, 'b': 20}
# dict_['c']


# IndexError: - ошибка индекса(не входит в диапазон списка)
# list_ = [1, 2, 3]
# list_[4]


# TypeError: - ошибка типов, когда тип объекта не подходит к операции
# string_ = 'youtube'
# num1 = 12
# string_ + num1


# ValueError: - ошибка значения, когда тип объекта подходит для операции, но значение нет.
# int(12.5) - ok
# int(12) - ok
# print(int('103')) -ok
# print(int('asadasd')) - ValueError:
# from math import sqrt
# print(sqrt(-25)) - ValueError:







# ошибка - проблема в синтаксисе кода. Например: нет скобки , двоеточия, отступа и т д

# SyntaxError: - синтаксическая ошибка 
# for i in range(1, 10)
#     print(i)

# IndentationError: - ошибка отступа
# for i in range(1, 10):
# print(i)    

# TabError - ошибка табуляции(смешивание пробелов и табуляций)
# for i in range(1, 10):
#       print(i)




# try:
#     print('Hello')
#     print(10 / 0)
#     print('World')
# except:
#     print('что-то пошло не так')    
# else:
#     print('try отработал без ошибок')    
# finally:
#     print('я отработаю в любом случае')    

# try:
#     попытка выполнить код, которая  потенциально может вызвать исключение
# except:
#     обработка исключений - сработает, если в try есть исключение
# else:
#     выполняется, если try пошел без исключений 
# finally:
#     выполняется в любом случае            


# try:
#     print(c)
# except Exception as error:
#     print(error)

# print('другой участок кода')        
# 10 + 10

# a = {'a': 10, 'b': 20}
# try:
#     print(10 / 0)
#     print(a['d'])
# except KeyError:
#     print('Нет такого ключа')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')       

# print('Другой участок кода')     

# b = [1, 2, 3]
# try:
#     print(b[10])
#     print(b.get('3'))
# except (IndexError, AttributeError):
#     print('нет такого индекса и метода')    

# raise - оператор для генерации собственных исключений 
# raise название исключения(описание исключения)

# temperature = int(input())
# if temperature > 100:
#     raise Exception('температура не может быть > 100')
# print('еще какойто код')    


# num1 = 10
# num2 = 0
# try:
#     num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')    

# if num2 != 0:
#     num1 / num2
# else:
#     print('На ноль делить нельзя')        


# try:
#     for i range(1, 10)
#     print(i)
# except SyntaxError: - # нельзя обработать 
#     print('непправильно написан код')    
   
# inp1 = input()
# try:
#     list_ = []
#     data = inp1.split()
#     for number in data:
#         list_.append(int(number))
#     print(list_)
# except:
#     raise TypeError('Данный элемент не является числом!')



