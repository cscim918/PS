E, S, M = map(int, input().split())
E_cnt, S_cnt, M_cnt, cnt = 1, 1, 1, 1

while True:
    if E == E_cnt and S == S_cnt and M == M_cnt:
        break
    E_cnt+=1; S_cnt+=1; M_cnt+=1; cnt+=1
    if E_cnt >= 16: E_cnt -= 15
    if S_cnt >= 29: S_cnt -= 28
    if M_cnt >= 20: M_cnt -= 19

print(cnt)
