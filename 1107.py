import sys
input = sys.stdin.readline
def check(num):
    num = list(str(num))
    for i in num:
        if i in s:
            return False
    return True

N = int(input())
M = int(input())
s = list(input().strip())
result = abs(N - 100)
for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i-N))
print(result)