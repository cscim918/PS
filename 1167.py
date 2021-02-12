import sys
from collections import deque
input = sys.stdin.readline
def BFS(i):
    q = deque()
    q.append([0,i])
    max_v = 0
    max_d = 0
    vis.add(i)
    while q:
        d, vertex = q.popleft()
        if d > max_d:
            max_d = d
            max_v = vertex
        for element in graph[vertex]:
            next_vertex, next_d = element
            if next_vertex not in vis:
                q.append([d+next_d, next_vertex])
                vis.add(next_vertex)
    return max_d, max_v

V = int(input())
graph = {}

for i in range(V):
    s = list(map(int, input().split()))[:-1]
    index = s.pop(0)
    graph[index] = []
    while s:
        j = s.pop(0)
        value = s.pop(0)

        graph[index].append([j,value])

vis = set()
a,b = BFS(1)
vis.clear()
answer, _ = BFS(b)
print(answer)