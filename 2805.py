import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int,input().split()))
s, e = 1, max(a)

while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for i in a:
        if i >= mid:
            cnt += i - mid
    if cnt >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)