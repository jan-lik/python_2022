def is_chetn(x):
    if x % 2 == 0:
        return True
    return False

a = range(1, 20, 1)
b = list(filter(is_chetn, a))
print(b)