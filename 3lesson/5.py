# В файле хранятся числа, нужно выбрать чётные и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 
# Получить: [(2, 4), (8, 64), (38, 1444)]

def f(x):
    return x**2
list = [1, 2, 3, 5, 8, 15, 23, 38]
list = [(i, f(i)) for i in list if i % 2 == 0]
print(list) # [(2, 4), (8, 64), (38, 1444)]