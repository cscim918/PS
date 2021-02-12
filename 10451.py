import sys
sys.setrecursionlimit(2000) # 최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다
input = sys.stdin.readline

def dfs(x):
    vis[x] = True
    num = nums[x]
    if not vis[num]:
        dfs(num)


for i in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    vis = [True] + [False] * n
    res = 0

    for i in range(1, n+1):
        if not vis[i]:
            dfs(i)
            res += 1
    print(res)