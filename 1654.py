import sys
input = sys.stdin.readline

k, n = map(int, input().split())
s = []
for i in range(k):
    s.append(int(input()))
start, end = 1, max(s)

while start <= end:
    m = (start+end)//2
    cnt = 0
    for i in s:
        cnt += i // m
    if cnt >= n:
        start = m + 1
    else:
        end = m - 1
print(end)