def my_lower(x):
    if isinstance(x, str):
        return x.lower()
    else:
        return x


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [my_lower(x) for x in L1 if isinstance(x, str)]
print(L2)

print(10 ** 3)


classmates = ['Michael', 'Bob', 'Tracy']
var = len(classmates)
print(var)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])