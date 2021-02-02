n = int(input())

a = []

for i in range(n):
    a.append(input().split())

a.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(a[i][0])