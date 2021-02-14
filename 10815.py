import sys
input = sys.stdin.readline
N = int(input())
sn = list(map(int,input().split()))
M = int(input())
sm = list(map(int,input().split()))
sn.sort()
for i in sm:
    low, high = 0, N
    while low <= high:
        mid = (low+high) // 2
        if 0 <= mid < N:
            if sn[mid] < i:
                low = mid + 1
            else:
                high = mid - 1
        else:
            break
    if 0 <= high + 1 < N:
        if sn[high+1] == i:
            print(1, end=" ")
        else:
            print(0, end=" ")
    else:
        print(0, end=" ")