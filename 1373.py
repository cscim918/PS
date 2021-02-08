# 1. 10진수로 변환 후 8진수로 변환
import sys
n = list(sys.stdin.readline())
a = 0
for i in range(len(n)):
    if n[i] == '1':
        a += 2**(len(n)-1-i)
b = ''
while a != 0:
    b += str(a%8)
    a = a // 8

print(b[::-1])

# 2. 파이썬 내장 함수 이용

print(oct(int(input(), 2))[2:])