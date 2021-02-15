N = int(input())
q = [input() for _ in range(N)]

def quad(x1, y1, x2, y2, n):
    if n == 1:
        return q[y1][x1]
    a = n // 2
    # 4등분
    p1 = quad(x1, y1, x1+a, y1+a, a)
    p2 = quad(x1+a, y1, x1+n, y1+a, a)
    p3 = quad(x1, y1+a, x1+a, y1+n, a)
    p4 = quad(x1+a, y1+a, x1+n, y1+n, a)

    if p1==p2==p3==p4 and len(p1) == 1:
        return p1
    return "(" + p1 + p2 + p3 + p4 + ")"

print(quad(0,0,N, N, N))