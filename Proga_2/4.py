a = [1,5,7]
b = [2,3,7]
c = list(zip(a,b))
print(list(map(lambda x: x[0]*x[1], c )))
print(sum(list(map(lambda x: x[0]*x[1], c ))))