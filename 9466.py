import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(x):
    global res
    vis[x] = True
    cycle.append(x) # 사이클을 이루는 팀을 확인
    num = nums[x]
    if vis[num]: # 방문 가능한 곳이 끝났는지
        if num in cycle: # 사이클 가능 여부
            res += cycle[cycle.index(num):] # 사이클 되는 구간부터 팀 결성
        return
    else:
        dfs(num)

for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    vis = [True] + [False] * n
    res = []

    for i in range(1, n+1):
        if not vis[i]: # 방문 안했으면
            cycle=[]
            dfs(i) # dfs 함수 실행
    print(n-len(res)) # 팀에 없는 사람 수
