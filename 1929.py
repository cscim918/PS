# import sys
#
# a, b = map(int,sys.stdin.readline().split())
#
# for i in range(a, b+1):
#     cnt = 0
#     for j in range(2, int(i**0.5)+1):
#         if(i%j==0):
#             cnt +=1
#     if(cnt==1):
#         print(j)

import sys

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

a,b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    if isPrime(i):
        print(i)