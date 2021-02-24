n, m = map(int, input().split())
s = list(map(int, input().split()))
sum = [0] * (n+1)
for i in range(1,n+1):
    sum[i] = sum[i-1] + s[i-1]
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if sum[j] - sum[i] == m:
            ans +=1
            break
print(ans)
