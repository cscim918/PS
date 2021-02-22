from itertools import permutations

n = int(input())
s = permutations(list(map(int, input().split())))
res = 0
for a in s:
    sum = 0
    for i in range(n-1):
        sum += abs(a[i]-a[i+1])
    res = max(res, sum)
print(res)