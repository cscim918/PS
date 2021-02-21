N, K = map(int, input().split())

a = list(int(input()) for _ in range(N))

cnt = 0

for i in a[::-1]:
    if i > K:
        continue
    cnt += K // i
    K %= i

print(cnt)