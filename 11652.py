n = int(input())

dict = {}

for i in range(n):
    m = int(input())
    if m in dict:
        dict[m] += 1
    else:
        dict[m] = 1

dict = sorted(dict.items(),key=lambda x: (-x[1], x[0]))
print(dict[0][0])