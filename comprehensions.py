""" comprehensions (генераторы) """

# a = []
# for i in range(10):
#     a.append(i)
# print(a) # - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list2 = [i for i in range(10)]
# print(list2) # - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


""" comprehensions - короткий способ записи циклов для создания коллекций(словари, списки, множества, кортежи). """

# list3 = [выражение for выражение in итерируемый_объект]

# names = ['Alina', 'Donny', 'Suban', 'Zalina']
# # guests = []
# # for name in names:
# #     guests.append(name + '10')
# # print(guests)    ['Alina10', 'Donny10', 'Suban10', 'Zalina10']
# guests = [name + '10' for name in names]
# print(guests) # - ['Alina10', 'Donny10', 'Suban10', 'Zalina10']


# names = ['John', 'Mike', 'Linda', 'Dinara', 'Farida', 'Aliya']
# guests = []
# for name in names:
#     if name[0] == 'A':
#         guests.append(name)
# print(guests)        # - ['Aliya']

# guests1 = [name for name in names if name.startswith('A')]
# print(guests1)        # - ['Aliya']

# nums = [1, 2, 3, 4, 5, 6]
# new_nums = []
# for i in nums:
#     if i % 2 ==0:
#         new_nums.append(i + 0.3)
#     else:
#         new_nums.append(i + 0.6)    
# print(new_nums)

# new_nums2 = [num + 0.3 for num in nums if num % 2 == 0 else num + 0.6] # Syntax Error

# тернарный оператор 
# i + 0.3 if i % 2 == 0 else i + 0.6
# """new_num3 = [num + 0.3 if num % 2 == 0 else num + 0.6 for num in nums]
# print(new_num3)  -  new_nums.append(i + 0.3) 
# [тернарный_оператор for элемент in итер_об]"""

# nums = [4, 3, 5, 8, 7, 1, 9]
# new_nums = [num + 0.6 if num % 2 != 0 else num + 0.3 for num in nums if num > 5]
# print(new_nums) # - [8.3, 7.6, 9.6]

# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = []
# for i in lists:
#     for j in i:
#         new_list.append(j)
# print(new_list)        # - [1, 2, 3, 4, 5, 6, 7, 8, 9]

# new_list = [j for i in lists for j in i]
# print(new_list)     # -  [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = (i for i in range(10))
# print(set(a))
# print(list(a))
# print(a)
# print(tuple(a))


# dict_ = {'a': 1, 'b': 2, 'c': 3}
# # b = {}
# # for k, v in dict_.items():
# #     b[k] = v
# # print(b)  -  {'a': 1, 'b': 2, 'c': 3}

# c = {k: v for k, v in dict_.items()}
# print(c) # - {'a': 1, 'b': 2, 'c': 3}

# from curses.ascii import isdigit


# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(num) for num in str_list]
# print(int_list)

# list_ = [False if num % 2 != 0 else True for num in range(1, 10)]
# # print(list_)

# ist_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['Shorter' if len(str_) <= 4 else 'Longer' for str_ in ist_name]
# print(new_list)

# list_ = {num: num ** 2 for num in range(1, 11)}
# print(list_)

# n = int(input())
# dict_ = {num: num ** 2 for num in range(1, 501) if num % n == 0}
# print(dict_)



# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [num for num in string_.split() if num.isdigit()]
# print(list_)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {key1: key2 for key1, val1 in dict_.items() for key2, val2  in val1.items() if val2 == max(val1.values())}
# print(new_dict)