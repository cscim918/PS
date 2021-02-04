a = list(input())
for i in range(len(a)):
    if a[i].isupper():
        if ord(a[i]) + 13 <= 90:
            a[i] = chr(ord(a[i])+13)
        else:
            a[i] = chr(ord(a[i])-13)

    elif a[i].islower():
        if ord(a[i]) + 13 <= 122:
            a[i] = chr(ord(a[i])+13)
        else:
            a[i] = chr(ord(a[i])-13)

for i in a:
    print(i, end="")