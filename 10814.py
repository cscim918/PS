n = int(input())
m = []
for i in range(n):
    m.append(list(input().split()))
m.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(m[i][0], m[i][1])