import sys
# 1. find 함수 사용
a = sys.stdin.readline()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(a.find(i), end=" ")

# 2. index 함수 사용
for i in range(len(alpha)):
    if alpha[i] in a:
        print(a.index(alpha[i]), end=" ")
    else:
        print(-1, end=" ")