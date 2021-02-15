import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def merge_sort(start, end):
    global swap, arr
    size = end - start
    mid = (start + end) // 2
    if size <= 1:
        return

    # divide
    merge_sort(start, mid)
    merge_sort(mid, end)

    # merge
    new_arr = []
    i, j = start, mid
    cnt = 0
    while i < mid and j < end:
        if arr[i] > arr[j]:
            new_arr.append(arr[j])
            j += 1
            cnt += 1
        else:  # arr[idx1] < arr[idx2]
            new_arr.append(arr[i])
            i += 1
            swap += cnt

    while i < mid:
        new_arr.append(arr[i])
        i += 1
        swap += cnt
    while j < mid:
        new_arr.append(arr[j])
        j += 1

    # reflect
    for t in range(len(new_arr)):
        arr[start + t] = new_arr[t]


n = int(input())
arr = list(map(int, input().split()))
swap = 0
merge_sort(0, n)
print(swap)