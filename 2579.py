n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

dp = []
dp.append(a[0])
dp.append(max(a[0]+a[1], a[1]))
dp.append(max(a[0]+a[2],a[1]+a[2]))

for i in range(3, n): # 3개를 미리 넣어야 된다.
    dp.append(max(dp[i-3]+a[i]+a[i-1],dp[i-2]+a[i]))

print(max(dp))