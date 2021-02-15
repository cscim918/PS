def hanoi(n, a, b, c):
    if n == 1:
        m.append([a,c])
    else:
        hanoi(n-1, a, c, b)
        m.append([a,c])
        hanoi(n-1, b, a, c)
m=[]
hanoi(int(input()), 1, 2, 3)
print(len(m))
print('\n'.join([' '.join(str(i) for i in row) for row in m]))