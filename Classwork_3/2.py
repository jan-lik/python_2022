words = input().split()
print(words)
words_set = [set(word) for word in words]
print(words_set)
a = words_set[0]

for word in words_set:
    a = a.intersection(word)
print(a)