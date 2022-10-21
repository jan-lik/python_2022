def sr(spisok, n):
    a = len(spisok)
    b = []
    for i in range(a):
        b.append(0)
        if a - i <= n:
            for j in range(i, i+n):
                b[i] = b[i] + spisok[j]**2
            b[i] = (b[i] /n) ** 0.5
        else:
            for j in range(i, a):
                b[i] = b[i] + spisok[j]**2
            b[i] = (b[i] / (a -i)) ** 0.5
    print(b)