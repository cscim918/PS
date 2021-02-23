import sys
input = sys.stdin.readline
def dfs(i, sum):
    global cnt
    if i >= n:
        return
    sum += a[i]
    if sum == s:
        cnt += 1
    dfs(i+1, sum - a[i])
    dfs(i+1, sum)

n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)