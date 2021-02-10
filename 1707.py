import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(now, group):
    vis[now] = group
    for i in a[now]:
        if vis[i] == 0:
            if not dfs(i, -group):
                return False
        elif vis[i] == vis[now]:
            return False
    return True

k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    vis = [0] * (v+1)
    for _ in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    ans = True
    for i in range(1, v+1):
        if vis[i] == 0:
            ans = dfs(i, 1)
            if not ans:
                break
    print("YES" if ans else "NO")
