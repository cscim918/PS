N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

m = 0
z = 0
p = 0

def cut_paper(x, y, n):
    global m, z, p
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(paper[i][j] != check):
                for k in range(3):
                    for l in range(3):
                        cut_paper(x+k*n//3, y+l*n//3, n//3)
                return

    if(check==-1):
        m += 1
    elif(check==0):
        z += 1
    else:
        p += 1

cut_paper(0,0,N)
print(m)
print(z)
print(p)