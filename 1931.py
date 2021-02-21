import sys
input = sys.stdin.readline
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

a = sorted(a, key=lambda a:a[0])
a = sorted(a, key=lambda a:a[1])
end = 0
cnt = 0
for i in a:
    if i[0] >= end:
        end = i[1]
        cnt += 1
print(cnt)