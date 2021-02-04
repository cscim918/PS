a = list(input())
s = []
c = 0

for i in range(len(a)):
    if a[i] == "(":
        s.append("(")
    else:
        if a[i-1] == "(":
            s.pop()
            c += len(s)
        else:
            s.pop()
            c += 1
print(c)