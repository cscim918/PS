# 1. 아스키 코드 활용

# a = [0] * 26
# for i in input():
#     a[ord(i)-ord('a')] += 1
#
# print(*a)

# 2. 튜플 활용
a = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
result = {}
for i in alpha:
    result[i] = a.count(i)

string = ""
for i in result.values():
    string += str(i) + " "

print(string.rstrip())