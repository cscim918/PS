# 1. Counter 이용
from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
sn = list(map(int,input().split()))
M = int(input())
sm = list(map(int,input().split()))
sn = Counter(sn)
for i in sm:
    print(sn[i], end=" ")

# 2. dictionary로 key값으로 value 뽑아오기
from sys import stdin
N = int(input())
arr_n = list(map(int,stdin.readline().split()))
M = int(input())
arr_m = list(map(int,stdin.readline().split()))
dic = dict()
for i in arr_n:
    try :
        dic[i] += 1
    except:
        dic[i] = 1
for i in arr_m:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")