

# name_of_list  = ['Helloworld!']
# string = name_of_list[0]
# half_of_string = len(string) // 2 
# if len(string) % 2 == 0:
#     new_list = list(string[half_of_string:] + string[0:half_of_string])
# else:
#     len(string) % 2 != 0
#     new_list = list(string[half_of_string + 1:] + string[0:half_of_string + 1])
    
# print(new_list)    

# list1 = [1 ,2, 3, 3, 5, 6, 7, 3]
# list2 = [8, 9 , 12, 1, 3, 4, 5]
# res = []
# # for i in list1:
#     for j in list2:
#         if i == j:
#             res.append(i)
# print(res)            


# list_ = [1, 1, 3]
# for i in list_:
#     if list_.count(i) > 1:
#         print('YES')
#         break
#     else:
#         print('ERROR')
#         break


""" словари """

# task 1


# a
# university = {'программирование': 159, 'экономика': 98, 'медицина': 82}
# university['экономика'] = 120
# print(university)

# b 
# university['лингвистика'] = 56
# print(university)
# university.update({'лингвистика': 57})
# print(university)

# с
# university.setdefault('лингвистика', 60)
# # print(university)
# print(university.pop('медицина'))
# # print(university)
# print(sum(list(university.values())))

#  Task 2

# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# new_dict = {}
# for key, val in dict_.items():
#     new_dict.update({val: key})
# print(new_dict)

# Task 3

# count = int(input('How many guests do you want invite? '))
# guests = {}
# for i in range(1, count + 1):
#     name = input('enter guest name: ')
#     guests.setdefault(i, name)
# print(guests)    

# Task 4

# my_list = [{'potato':10, 'milk': 1, 'eggs': 20, 'brad': 2}]

# while my_list:
#     product_to_remove = input()
#     for products in my_list:
#         if product_to_remove in products:
#             del products[product_to_remove]
#             print(my_list)
#     if not any(my_list):
#         break
# print('its time to pay')

# from string import ascii_lowercase
# a = {}


# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = a.copy()

# for k, v in a.items():
#     if v % 2 == 0:
#         b[k] = 2
#     else:
#         continue
# print(b)    



# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(a.items()):
#     if v == None:
#         a.pop(k)
# print(a)  




# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for key in a.keys():
#     a.update({key: a[key] / 5})
# print(a)    


# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)
# print(a)        
   
# a = {'a': 1, 'b': 2, 'c': 3}
# for k, v in list(a.items()):
#     del a[k]
#     a[v] = k
# print(a)

# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)

# list_ = [num ** 2 if num % 2 == 0 else num for num in range(1, 11)]
# print(list_)

# list_ = [True if num % 2 == 0 else False for num in range(1, 10)]
# print(list_)

# list_x = ['X--', '--X', '++X', 'X++']
# x = 0
# for num in list_x:
#     if num == '++X' or 'X++':
#         num = x + 1
#     else:
#         num = x - 1
# print(x)        


# dict_ = {'first': 1, 'second': 2, 'third': 3}

# a = {key: 'even' if val % 2 == 0 else 'odd' for key, val in dict_.items()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [num for num in string_.split() if num.isnumeric()]
# print(list_)


# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

#  list_ = []

num1 = input()
for num in num1:
    if num1 % num1 == 0:
        print('Частное': )
    elif num1 % num2 != 0:
        print('Остаток': )