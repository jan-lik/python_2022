a = [1, 2, 3, 4, 5, 6]
b = [2, 4, 6, 8]
c = []
f = []
for item in a:
    if item in b and item not in c:
        c.append(item)
print(c)
#Пересекли два списка
d = [7, 8, 9, 10, 11, 12, 2, 4]
e = [8, 10, 12, 14, 2, 4]
for item in d:
    if item in e and item not in f:
        f.append(item)
print(f)
# Пересекли еще два списка
# Объединим два полученных спсика
set_c = set(c)
for el in f:
    if el not in c :
        c.append(el)

print(c)