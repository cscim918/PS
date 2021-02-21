N = int(input())
p = []
n = []
e = []
for i in range(N):
    a = int(input())
    if a > 1:
        p.append(a)
    elif a < 0:
        n.append(a)
    else:
        e.append(a)

p.sort(reverse=True)
n.sort()

result = 0
if len(p)%2==0:
    for i in range(0, len(p)-1, 2):
        result += p[i] * p[i+1]
if len(p)%2!=0:
    for i in range(0, len(p)-1, 2):
        result += p[i] * p[i+1]
    result += p[-1]

if len(n)%2==0:
    for i in range(0, len(n)-1, 2):
        result += n[i]*n[i+1]
if len(n)%2!=0:
    for i in range(0, len(n)-1, 2):
        result += n[i]*n[i+1]
    if 0 not in e:
        result += n[-1]

result += sum(e)
print(result)