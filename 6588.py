def isPrime(n):
    num = [1] * n
    for i in range(2, int(n**0.5)+1):
        if num[i] == 1:
            for j in range(i+i,n,i):
                num[j] = 0
    return num

num = isPrime(1000000)

while True:
    n = int(input())
    if n==0:
        break
    for i in range(3,n//2+1):
        if num[i] and num[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            break