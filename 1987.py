import sys
input = lambda: sys.stdin.readline().strip()

r, c = map(int,input().split())
a = [list(map(lambda x : ord(x)-65, input())) for i in range(r)]
check = [0] * 26

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, z):
    global ans
    ans = max(ans, z)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and check[a[nx][ny]] == 0:
            check[a[nx][ny]] = 1
            dfs(nx, ny, z+1)
            check[a[nx][ny]] = 0

ans = 1
check[a[0][0]] = 1
dfs(0, 0, ans)
print(ans)