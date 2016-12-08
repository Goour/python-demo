def is_palindrome(x):
    l = list(str(x))
    impasse = True
    for i in range(len(l)):
        if l[i] != l[len(l) - i - 1]:
            return False
    return impasse


pass

output = filter(is_palindrome, range(1, 1000))
print(list(output))
