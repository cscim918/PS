n = int(input())
s = list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    sum = 0
    for j in range(i):
        if s[i] > s[j]:
            sum = max(sum, dp[j])
    dp[i] = s[i] + sum

print(max(dp))

