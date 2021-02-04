import sys
while True:
    a = sys.stdin.readline().rstrip('\n')
    if not a:
        break
    so, dae, num, spa = 0, 0, 0, 0
    for i in a:
        if i.islower():
            so += 1
        elif i.isupper():
            dae += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            spa += 1
    print(so, dae, num, spa)