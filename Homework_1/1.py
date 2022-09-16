m = 6
n = 5
#a=[[2 for i in range (j), 0 for i in range(j, j+1), 1 for i in range(j+1, m) for j in range (n):
a=[[i+j*6 for i in range(m)]for j in range(n)]
print(a)
#0  1  2  3  4  5
 #6  7  8  9 10 11
#12 13 14 15 16 17
#18 19 20 21 22 23
#24 25 26 27 28 29
#[[ i * j for j in range(m)] for i in range(n)]