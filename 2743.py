import sys
a = sys.stdin.readline().rstrip('\n')
b = []
for i in a:
    if not str(i):
        break
    else:
        b.append(str(i))

print(len(b))