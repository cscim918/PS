n=int(input())
A=[1,2,4]
for i in range(3,10):
    A.append(A[i-3]+A[i-2]+A[i-1])

for j in range(n):
    m = int(input())
    print(A[m-1])