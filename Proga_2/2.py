a = input("Ведите список").split()
a = map(int,a)
def is_square(b):
    return b in [i**2 for i in range(1,10)]
a_filtered = list(filter(is_square,a))
print(a_filtered)