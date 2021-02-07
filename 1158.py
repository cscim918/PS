import sys

n, k = map(int, sys.stdin.readline().split())

s1 = [i for i in range(1,n+1)]
s2 = []
num = 0
for i in range(n):
    num += k-1
    if num >= len(s1):
        num = num % len(s1)
    s2.append(s1.pop(num))

print("<%s>" % (", ".join(map(str, s2))))
# print("<",", ".join(s2)[:],">",sep='')