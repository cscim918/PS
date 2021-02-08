n = int(input())
sum = 1
for i in range(1,n+1):
    sum *= i
a = list(str(sum))
cnt = 0
for i in a[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break