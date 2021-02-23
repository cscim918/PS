import sys
from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
pwd = sorted(list(map(str, sys.stdin.readline().split())))
comb = combinations(pwd, l)

for i in comb:
    cnt = 0
    for letter in i:
        if letter in vowels:
            cnt += 1
    if 1<= cnt <= l-2:
        print(''.join(i))


