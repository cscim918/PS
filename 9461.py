dp = [1, 1, 1]

for i in range(3, 101):
    dp.append(dp[i-3] + dp[i-2])

n = int(input())
for i in range(n):
    m = int(input())
    print(dp[m-1])