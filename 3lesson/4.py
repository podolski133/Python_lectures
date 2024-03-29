# List Comprehension - нужен для быстрого создавания списков

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]

# Создаём список от 1 до 100 из чётных чисел.

# list = [] # создали список

# for i in range(1, 21): # пробегаемся от 1 до 21
#     if(i%2 == 0): # проверяем условие, если остаток от деления на 2 равен 0
#         list.append(i); # то в этом случае добавляем в лист 

# print(list) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Как сделать более красиво:

list = [i for i in range(1,21) if i % 2 == 0]
print(list) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

list = [(i, i) for i in range(1,21) if i % 2 == 0]
print(list) # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

def f(x):
    return x**3
list = [f(i) for i in range(1,21) if i % 2 == 0]
print(list) # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

list = [(i, f(i)) for i in range(1,21) if i % 2 == 0]
print(list) # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), 
# (18, 5832), (20, 8000)]