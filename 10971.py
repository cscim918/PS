import sys
input = sys.stdin.readline

def dfs(start, cur, cost):
    global s, visit, minCost

    if start == cur and visit.count(False) == 0:
        minCost = min(minCost, cost)
    for i in range(n):
        if not s[cur][i] == 0 and not visit[i]:
            visit[i] = True
            dfs(start, i, cost+s[cur][i])
            visit[i] = False

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]

minCost = sys.maxsize
visit = [False for _ in range(n)]
dfs(0, 0, 0)

print(minCost)