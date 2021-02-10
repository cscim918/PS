import sys

n, m = map(int, sys.stdin.readline().split())

g = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
visited = [0] * (n+1)

def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        for i in g[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

a = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        a += 1

sys.stdout.write(str(a))