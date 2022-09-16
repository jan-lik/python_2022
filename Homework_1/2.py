m = 6
n = 5
a = [[(i == j)*0 + (i < j) * 2 + (i > j) for i in range(m)] for j in range(n)]
#a=[[i+j*6 for i in range(m)]for j in range(n)]
print(a)
#2 for i in range(j), 0 for i in range(j, j+1), 1 for i in range(j+1, m)