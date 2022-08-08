""" словари  (dict) """

# Словарь - это изменяемый, итерируемый тип данных Состоят из ключей из пар : ключ: значение
# Ключи могут быть только неизменяемые типы данных: (tuple, str, int, None, bool), а значениями любые.
# Ключи должны быть уникальными.

# dict_ = {}

# passport = {'name': 'Donny', 'last_name': 'Aks', 'age': 35, 'gender': 'M', 'birthday': '03.07.1987'}

# print(passport['name']) # 'Donny'
# print(passport['age']) # 35
# print(passport[0]) # ERROR


# dict2 = dict(name = 'Donny', last_name = 'Aks', age = 19)
# print(dict2) # {'name': 'Donny', 'last_name': 'Aks', 'age': 19}

# dict3 = dict.fromkeys(['a', 'b'], 25)
# print(dict3) # {'a': 25, 'b': 25}

# dict4 = dict.fromkeys(['a', 'b'])
# print(dict4) # {'a': None, 'b': None}

# dict5 = dict([('name', 'John'), ('last_name', 'Watson')])
# print(dict5) # {'name': 'John', 'last_name': 'Watson'}


""" Методы словарей """

# passport = {'name': 'Donny', 'last_name': 'Aks', 'age': 35, 'gender': 'M', 'birthday': '03.07.1987'}

# passport['name'] # Donny
# passport['id'] # KeyError
# print(passport.get('name')) # Donny
# print(passport.get('id')) # None
# dict.get(key, None) - отдает второе указанное значение (по умолчанию None) 
# print(passport.get('ID', 'Нет такого ключа!')) # Нет такого ключа!


# passport.setdefault(key, default) - отдает значение указанного ключа,
#  если его нет - создает его со значением default(по умолчанию - None)

# print(passport.setdefault('age')) # 35
# # print(passport.setdefault('ID')) # {'name': 'Donny', 'last_name': 'Aks', 'age': 35, 'gender': 'M', 'birthday': '03.07.1987', 'ID': None}
# print(passport.setdefault('ID', 234243234))
# print(passport) # {'name': 'Donny', 'last_name': 'Aks', 'age': 35, 'gender': 'M', 'birthday': '03.07.1987', 'ID': 234243234}


# # passport.update({key: value}) - принимает в себя другой словарь, и обновляет исходный словарь за счет него
# dict8 = {'name': 'Майрам', 'age': 27, 'name': 'Саша'} # {'name': 'Саша', 'age': 27} - перезаписывает ключ
# passport.update(dict8)
# print(passport) # {'name': 'Саша', 'last_name': 'Aks', 'age': 27, 'gender': 'M', 'birthday': '03.07.1987'}


# a = {'a': 10, 'b': 20}
# a['c'] = 30
# a['b'] = 40
# print(a) # - {'a': 10, 'b': 40, 'c': 30}


# dict10 = {'name': 'Алия', 'last_name': 'Алиева', 'age': 25}
# dict10.pop('name')
# # print(dict10) # - {'last_name': 'Алиева', 'age': 25}
# deleted_el = dict10.pop('ID', 'Нет такого ключа!')
# print(deleted_el) # - Нет такого ключа!

# dict10.popitem()
# print(dict10) # - {'name': 'Алия', 'last_name': 'Алиева'} 

# deleted_el = dict10.popitem()
# print(deleted_el)
# print(dict10) # -  ('age', 25)
# {'name': 'Алия', 'last_name': 'Алиева'}

# dict10.clear()
# print(dict10) # - {}

# del dict10['age']
# print(dict10) # - {'name': 'Алия', 'last_name': 'Алиева'}


# iter_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# # for i in iter_dict:
# #     print(i) # - keys a b с в

# for i in iter_dict:
#     print(iter_dict[i]) # - Values 10 20 30 40

""" keys(), values(), items() """

# iter_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# k = iter_dict.keys()
# #print(k) # - dict_keys(['a', 'b', 'c', 'd'])
# # for key in k:
# #     print(key)

# v = iter_dict.values()
# #print(v) # - dict_values([10, 20, 30, 40])
# # for value in v:
# #     print(value)

# it = iter_dict.items()
# #print(it) # - dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
# for key, value in it:
#     print(f'ключи {key}, значения {value}') # ключи a, значения 10
#                                             # ключи b, значения 20
                                            # ключи c, значения 30
                                            # ключи d, значения 40


# contacts = {'names': {'Aidar': 234242423, 'Atai': 454545454, 'Igor': 121232323}}
# # print(contacts['names']['Igor']) # - 121232323
# names = contacts['names']
# print(names['Igor']) # - 121232323

# # .copy() - копирует словарь
# contacts_copy = contacts.copy()

# from string import ascii_lowercase
# a = {}
# num = 1
# for i in ascii_lowercase:
#     a[i] = num
#     num += 1
# print(a) # - {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


# print(ord('a'))
# print(chr(97))

# a = ord('a')
# b = chr(


# alp = []
# for i in range(97, 123):
#     alp.append(chr(i))
# print(alp)
# dict = {}  
# for i in alp:
#     dict[i] = ord(i) - 96
# print(dict)      

# a = {}
# for i in range(26):
#     a[chr(i + ord('a'))] = i + 1
# print(a)    

# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#        'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#        'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#        'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#        'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#        'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# for key, value in emails.items():
#     for name in value:
#         print(name + '@' + key)



# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for v in a.values():
#     result = result * v
# print(result)    


# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# for k, v in a.items():
#     if v % 2 == 0:
#         b[k] = 2
#     else:
#         continue    
# print(b)        


# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = a.copy()
# for k, v in a.items():
#     if v == None:
#         del b[k]
# print(b)        

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k, v in a.items():
#     a[k] = v / 5
    
# print(a)    

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = a.copy()
# for k, v in b.items():
#     if v % 2 == 0:
#         del a[k]
# print(a)        




# a = {'a': 1, 'b': 2, 'c': 3}
# for k, v in a.items():
#     del a[k]
#     a[v] = k
# print(a)    

# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)




# a = {'a': 10, 'b': 9, 'c': 3}
# result = 0
# for k, v in a.items():
#     result = a['a'] * a['b'] * a['c']
# print(result)    


string = "pythonist"