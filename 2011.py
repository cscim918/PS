a = list(map(int, input()))
l = len(a)
dp = [0] * (l+1)

if a[0] == 0:
    print(0)
else:
    a = [0] + a
    dp[0] = 1
    dp[1] = 1

    for i in range(2, l+1):
        s = a[i]
        s2 = a[i-1]*10 + a[i]
        if s >= 1 and s <= 9:
            dp[i] += dp[i-1]
        if s2 >= 10 and s2 <= 26:
            dp[i] += dp[i-2]
    print(dp[l] % 1000000)