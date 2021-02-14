import sys
input = sys.stdin.readline
N, C = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
a.sort()
s, e = 1, a[-1]-a[0] # 공유기 간격을 어떻게 해야할지 모르니 최대거리와 최소거리의 중간부터 시작
while s <= e:
    mid = (s+e) // 2
    cnt = 1
    install = a[0]
    for i in range(1,N):
        if a[i] >= install + mid: # 설치 간격 충족
            cnt += 1
            install = a[i]
    if cnt < C: # 공유기 개수가 C보다 작으면 더 설치(간격을 좁혀야 한다)
        e = mid - 1
    else: # 공유기 개수가 C보다 많거나 같으면 덜 설치(간격을 넓혀야 한다)
        s = mid + 1
        b = mid # 중간에 mid 저장하는 이유는 개수를 만족할 때 간격을 늘리려다 다음에는 개수 만족 못시키고 while문 종료될 수 있기 때문에
print(b)