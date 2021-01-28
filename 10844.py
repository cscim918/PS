n = int(input())
A = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1,10):
    A[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            A[i][j] = A[i-1][1]
        elif j == 9:
            A[i][j] = A[i-1][8]
        else:
            A[i][j] = A[i-1][j-1] + A[i-1][j+1]

print(sum(A[n])%1000000000)