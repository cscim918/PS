n = int(input())

A = []

for i in range(n):
    [a,b] = (map(int, input().split()))
    s = [b,a]
    A.append(s)

A.sort()

for i in range(n):
    print(A[i][1],A[i][0])