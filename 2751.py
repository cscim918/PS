# pypy 제출, sorted 함수 이용
# n=int(input())
# num=[]
#
# for _ in range(n):
#     x = int(input())
#     num.append(x)
#
# for i in sorted(num):
#     print(i)

# pypy 제출, merge_sort 이용
def merge_sort(A, f, l):
    if f >= l: return
    m = (f+l) // 2
    merge_sort(A, f, m)
    merge_sort(A, m+1, l)
    B =[]
    i = f
    j = m+1
    while i <= m and j <= l:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for i in range(i, m+1):
        B.append(A[i])
    for j in range(j, l+1):
        B.append(A[j])
    for k in range(f, l+1):
        A[k] = B[k-f]

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

merge_sort(A, 0, len(A)-1)

for i in A:
    print(i)