def fib(x):
    n, a, b = 0, 0, 1
    while n < x:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


print(fib(2))
