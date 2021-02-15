def fractal(n):
    m = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            m.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            m.append(n[i % len(n)] * 3)
    return(list(m))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n//3)
    k += 1
for i in range(k):
    star = fractal(star)
for i in star:
    print(i)