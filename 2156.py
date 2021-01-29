n = int(input())

s = [0]
for i in range(n):
    m = int(input())
    s.append(m)

dp = [0]
dp.append(s[1])
if n > 1:
    dp.append(s[1]+s[2])
for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-2]+s[i],dp[i-3]+s[i-1]+s[i]))

print(dp[n])