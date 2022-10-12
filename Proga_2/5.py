with open('input.txt','r') as f:
    s = f.read()
    s = s.split('\n')
    b=[]
    for i in range(len(s)):
        a=''
        for j in range(len(s[-i-1])):
            a=a+s[-i-1][-j-1]
        b.append(a)
    for i in range(len(b)):
        print(b[i])