n = int(input())

A = []

for i in range(n):
    A.append(list(map(int, input().split())))

A.sort()

for i in range(n):
    print(A[i][0],A[i][1])