import sys
n = int(input())
s = []

for i in range(n):
    m = sys.stdin.readline().rstrip()
    cmd = m.split()[0]
    if cmd == 'push':
        s.append(int(m.split()[1]))
    elif cmd == 'pop':
        if not s:
            print('-1')
        else:
            print(s[-1])
            s.pop(-1)
    elif cmd == 'size':
        print(len(s))
    elif cmd == 'empty':
        if not s:
            print('1')
        else:
            print('0')
    elif cmd == 'top':
        if not s:
            print('-1')
        else:
            print(s[-1])