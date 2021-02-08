import sys

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

n = int(input())
for _ in range(n):
    t = list(map(int, input().split()))
    sum = 0
    for i in range(1, len(t)-1):
        for j in range(i+1, len(t)):
            sum += gcd(t[i], t[j])
    print(sum)