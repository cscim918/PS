N = int(input())
s = list(map(int, input().split()))
sum = 0
s.sort()
for i in range(N):
    for j in range(i+1):
        sum += s[j]
print(sum)