a=str(input())
b=[]
for i in a:
    b.append(a)
    a = a[1:]
for i in sorted(b):
    print(i)