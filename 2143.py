from itertools import combinations

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

acm, bcm = {}, {}
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        if acm.get(temp):
            acm[temp] += 1
        else:
            acm[temp] = 1
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        if bcm.get(temp):
            bcm[temp] += 1
        else:
            bcm[temp] = 1
ans = 0
for _,i in enumerate(acm):
    if bcm.get(t-i):
        ans += (acm[i]*bcm[t-i])
print(ans)