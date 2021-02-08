def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x


a, b = map(int, input().split())
print('1' * gcd(a, b))