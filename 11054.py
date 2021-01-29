n = int(input())
s = list(map(int, input().split()))

dpt = [0] * n
dpx = [1] * n
dpn = [1] * n

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dpx[i] = max(dpx[i], dpx[j]+1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if s[i] > s[j]:
            dpn[i] = max(dpn[i], dpn[j]+1)

for i in range(n):
    dpt[i] = dpx[i] + dpn[i]

print(max(dpt)-1)