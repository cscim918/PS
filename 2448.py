import math
s = ["  *   ", " * *  ", "***** "]

def star(n):
    for i in range(len(s)):
        s.append(s[i]+s[i]) # 현 단계에 삼각형을 뒤에 붙이고
        s[i] = ("   " * n + s[i] + "   " * n)

n = int(input())
k = int(math.log(int(n / 3), 2))
for i in range(k):
    star(int(pow(2,i)))

for i in range(n):
    print(s[i])