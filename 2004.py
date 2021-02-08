def five(n):
    a = 0
    while n!=0:
        n = n // 5
        a += n
    return a

def two(n):
    a = 0
    while n!=0:
        n = n // 2
        a += n
    return a

n, m = map(int, input().split())

if m==0:
    print(0)
else:
    print(min(two(n) - two(m) - two(n-m), five(n) - five(m) - five(n-m)))