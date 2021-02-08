import sys

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

a = int(sys.stdin.readline())

for i in range(1,a):
    if isPrime(i):
        print(i)