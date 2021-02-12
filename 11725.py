n = int(input())
t = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    t[a].append(b)
    t[b].append(a)

q = [1]
res = {}
check = [False] * (n+1)

while len(q)>0:
    parent = q.pop(0)
    for i in t[parent]:
        if not check[i]:
            res[i] = parent
            q.append(i)
            check[i]=True

for i in range(2, n+1):
    print(res[i])