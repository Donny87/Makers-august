""" Множества (set) """

# Множества - это изменяемый, неупорядочный тип данных.
# Содержит  в себе уникальные элементы и только неизменяемые типы данных.


# a = {}
# print(type(a)) # <class 'dict'>


# b = set()
# print(type(b))  # - <class 'set'>

# c = {'a', 1, True, (1, 2), 2.54, None}
# print(c) # - {'a', 2.54, (1, 2), 1, None}

# d = {1, 1, 1, 1, 1}
# print(d) # - {1}

# list_ = [1, 2, 3, 4, 4, 4, 3, 1]     - удаляет дубликаты
# a = set(list_)
# #print(a) # - {1, 2, 3, 4}
# print(list(a)) # - [1, 2, 3, 4] - список
