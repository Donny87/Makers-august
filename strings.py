# string1 = 'makers45%*'
# string2 = "bootcamp"
# print(string1, string2)

# string3 = 'maker's Bootcamp' - error

# string = "Makers's Bootcamp" - error
# print(string)


# sentence = 'John said: "I can code" ' - ковычки внутри ковычек
# print(sentence)

# sentence = 'I love Maker\'s Bootcamp'
# print(sentence) 

# string = "Dear friend, \n\nWelcome to Makers! \nEnjoy your time here with us!"
# print(string) - /n переносит на след строку


# string = """Dear friend, Welcome to hell!!!! U need a hard цщкл MF!!! """
# print(string)

# string = 'Thisi is very long string.\
# Ерe lenght of String in Python should not be more than 79 symbols.\
# Remember this. '
# print(string)

# languages = 'Languages:\n\t'
# description = 'Python backend language \n\tJavaScript: frontend language'
# print(languages, description)

# sentence = 'hello\vMakers\vBootcamp'
# print(sentence)
# hello
#      Makers
#            Bootcamp

# url = r'https://kaktus/\news\topics\read'
# print(url) - r сырая строка

# string1 = 'Makers'
# string2 = 'Bootcamp'
# print(string1 + ' ' + string2)

# num1 = '6'
# num2 = '7'
# result = num1 + num2
# print(result)

# string = 'makers'
# print(string  * 4)

# len()
# string = 'Makers Bootcamp'
# print(len(string))

# lenght = len('Don')
# print(lenght)


# sentence = 'Strings are ordered'
# print(sentence[1])

"""
[x:y]
"""

# string = 'Makers Bootcamp'
# # print(string[0:3]) --  срез 

# partstring = string[:6]

# print(partstring)

# string = 'Makers Bootcamp'
# print(string[::-1]) - строка наоборот

# string = 'Makers Bootcamp'
# print(string[1:6:2])

# word = 'dream'
# word[0] = 'c' - error

# word = 'dream'
# word = 'c' + word[1:]
# print(word) - cream

""" Методы строк"""

#find(string) , rfing r=справа

# string = 'Makers Bootcamp'
# print(string.find("Boot"))  -  7

# index(string)

# string = 'Makers Bootcamp'
# print(string.index ('camp')) - 11

#  replace(pattern, replace_pattern)
# string = 'Makers bootcamp'
# print(string.replace('camp', 'rock')) - Makers bootrock

# split(symbol) -> list
# string = 'makers boot*camp'
# print(string.split('*')) - ['makers boot', 'camp']




# full_name = input('Enter name and lastname: ').split()
# name = full_name[0]
# last_name = full_name[-1]
# print(name)
# print(last_name)

# isdigit(), isalpha(), isalnum(), islower(), isupper(), isspace(), istitle()

# string = '12345a'
# print(string.isdigit()) - false

# string = '12345a'
# print(string.isalnum()) - true (кроме знаков)

# string = 'makers'
# print(string.islower()) - true (isupper)

# string = '   '
# print(string.isspace()) - true

# string = 'Makers Bootcamp'
# print(string.istitle()) - true

"""upper() lower()"""

# string = 'Makers'
# # print(string.upper()) - MAKERS
# print(string.lower()) - makers

""" startswith(), endswith() """

# string = 'I love icecream'
# print(string.startswith('I')) - true

""" join(list) """

# list_ = ['m', 'k', 'r', 's']
# print(''.join(list_)) - mkrs

# list_ = ['1', '3', '4', '4']
# print(''.join(list_)) - 1344

# list_ = ['1', '3', '4', 4]
# print(''.join(list_)) - error only strings

""" capitalize() """

# string = 'bootcamp makers'
# print(string.capitalize()) - Bootcamp makers - делает заглавной первую букву

# print(string.title()) - Bootcamp Makers - каждой слово с заглавной

""" count() """

# string = 'Makers Bootcamp'
# print(string.count('o')) - 2 

# string = 'Makers Bootcamp aaaaa A'
# print(string[:6].count('a')) - 1 диапазон до 6 индекса

""" lsript(), rstrip(), strip() """

# password = '   qwerty'
# print(password.lstrip()) - qwerty - удаляет пробелы слева

""" partition(pattern) """
# string = 'hello makers bootcamp'
# print(string.partition('makers')) - ('hello ', 'makers', ' bootcamp')

""" swapcase() """

# string = 'camelcase'
# print(string.swapcase()) - CAMELCASE

""" zfill(width) """

# string = 'makers'
# print(string.zfill(9)) - 000makers

""" ljust(width, fillchar), rjust(width, fillchar) """ #- заполняют символами

# string = 'makers'
# print(string.ljust(9, '*')) - makers***

# string = 'makers'
# print(string.rjust(11, '&')) - &&&&&makers

""" format() """ 

# форматирование строк
# 1. %
# name = input()
# last_name = input()
# some_shit = "Wellcome, %s %s" % (name, last_name)
# print(some_shit) - #Wellcome, Don Aks


# name = input()
# lastname = input()
# variable = 'Hello,{} {}'.format(name, lastname)
# print(variable) - # Hello, don aks


# 3 метод  f''
# name = input()
# lastname = input()
# age = input()

# shit = f'Hello {name} {lastname}\n Your age is {age}'
# print(shit) -   #Hello Don  Aks
               #Your age is 33


""" МЕТОДЫ ПРОВЕРКИ"""

# string = 'My test string 123'
# print(string.isdigit()) - false
# print(string.isalpha()) - false
# print(string.isalnum()) - false
# print(string.isspace()) - false
# string.upper()
# string.lower() - замена регистра
# string.endswith('123'))- True



# num1 = 10
# num2 = 20

# num1 > num2 # False
# num1 == num2 # False
# num1 != num2 # True - неравенство
# num1 <= num2 # true



# str1 = 'apple'
# str2 = 'hello'
# print(str1 > str2)

# ord('a') # 97
# chr(97) # "a"
#ASCII Table - таблица номеров всех символов

# a = 'abcde'
# b = 'abced'

# print(sorted(a)) #['a', 'b', 'c', 'd', 'e']
# print(sorted(b)) #['a', 'b', 'c', 'd', 'e']

""" Форматирование строк/интерполяция"""

# stat = 'Привет, Фара! Приглашаю тебя на праздник!'

# name = 'Данияр'
# place = 'Бишкек'
# % - 1 метод 

# str5 = 'Привет, %s!' % name

# print(str5) # Привет, Данияр!

# 2 метод
# str6 = 'Привет, {}'.format(name)
# print(str6) - #Привет, Данияр

# 3 метод
# str7 = f'Hello {name} Welcome to {place}'
# print(str7)


""" Форматирование  строк - подстановка переменных в строку, создание динамической строки"""

# a = 'I\'m student'
# b = 'Идет ,бычок качается,\n\tВздыхает на ходу'
# print(b)

# # \n - newline
# # \t - tabular

""" Сырые строки """

# str8 = r'This is test string\n\t\n'
# print(str8) - #This is test string\n\t\n
# # raw

# windows_path = r'Users\Documents\new_folder'
# print(windows_path)

# string1 = 'Hello world'
# string2 = 'ell'
# print(string2 in string1)


"""#dir(obj) - функция возвращает список методов доступных переданному обЬекту
# print(dir(str1))"""
# str1 = 'hello'