import sys
s1 = list(sys.stdin.readline().strip())
s2 = []
n = int(sys.stdin.readline())
for i in range(n):
    c = sys.stdin.readline().strip()
    if c[0] == 'P':
        s1.append(c[2])
    elif c[0] == 'L' and s1 != []:
        s2.append(s1.pop())
    elif c[0] == 'D'and s2 != []:
        s1.append(s2.pop())
    elif c[0] == 'B' and s1 != []:
        s1.pop()

print(''.join(s1 + list(reversed(s2))))