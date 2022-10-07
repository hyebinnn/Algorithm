# 물병 (pypy3로 해야 맞음. 안그러면 시간초과) 1052

import sys

n, k = map(int, sys.stdin.readline().split())


def bottle(num):
    b = 0                   # 총 물병 갯수
    while 1:
        twin = num // 2
        remain = num % 2
        b += remain
        num = twin
        if num == 0:              # 끝까지 1병으로 합쳤을 때
            break
    return b


if k >= n:
    print(0)
else:
    buy = n
    while 1:
        if bottle(buy) <= k:
            print(buy - n)
            break
        else:
            buy += 1
