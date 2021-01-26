# def makeone2(x):
#     for i in range(2, x+1):
#         A[i] = A[i-1] + 1
#         if i%3 == 0 and A[i] > A[i//3] + 1:
#             A[i] = A[i//3] + 1
#         if i%2 == 0 and A[i] > A[i//2] + 1:
#             A[i] = A[i//2] + 1
#         print(A)
#     return A[x]
#

def makeone(x):
    d = [0, 0, 1, 1]
    for i in range(4, x+1):
        d.append(d[i-1]+1)

        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
    return d[x]


x=int(input())
A=[0 for x in range(x+1)]
print(makeone(x))

# 각 숫자에서 소요되는 최소 연산 횟수는 이전 단계 +1

