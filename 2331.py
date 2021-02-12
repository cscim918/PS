import sys

A, P = map(int, sys.stdin.readline().split())
s = [A]

while True:
    t = s[-1]
    v = 0
    while t:
        v += ((t%10)**P)
        t //= 10
    if v in s:
        sys.stdout.write(str(s.index(v)))
        break
    else:
        s.append(v)