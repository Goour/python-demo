from functools import reduce


def normalize(x):
    return x.capitalize()
    pass


def my_reduce(x, y):
    return x + y


L1 = ['adam', 'LISA', 'barT']
L2 = reduce(my_reduce, map(normalize, L1))
print(L2)
