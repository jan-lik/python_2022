m = 5
n = 5
a = [[(i <= j)*j + (i > j)*(i) for i in range (m)] for j in range (n)]
print(a)
#a = [[(i == j)*0 + (i < j) * 2 + (i > j) for i in range(m)] for j in range(n)]