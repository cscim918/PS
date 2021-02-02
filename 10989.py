import sys

n = int(sys.stdin.readline())
a = [0] * n
for i in range(n):
    a[int(sys.stdin.readline())] += 1

for i in range(n):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)