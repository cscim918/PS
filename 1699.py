n = int(input())

dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = i
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1

print(dp[n])

# n = int(input())
# dp = [0 for i in range(n + 1)]
# for i in range(1, n + 1):
#     s = [0]
#     for j in range(1,i):
#         if j > i:
#             break
#         s.append(dp[i - j] + 1)
#     dp[i] = min(s) + 1
#
# print(dp)