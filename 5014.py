from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    q = deque()
    q.append(i)
    visit = [0 for i in range(f)]
    visit[i] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dir[i]
            if 0 <= nx < f and visit[nx] == 0:
                q.append(nx)
                arr[nx] = arr[x] + 1
                visit[nx] = 1

f, s, g, u, d = map(int, input().split())

arr = [-1 for i in range(f)]
dir = [u, -d]
arr[s-1] = 0
bfs(s-1)
print(arr[g-1] if arr[g-1] != -1 else "use the stairs")
