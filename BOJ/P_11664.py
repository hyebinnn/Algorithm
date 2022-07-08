# 선분과 점

import sys

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, sys.stdin.readline().split())


def calculate(x1, y1, z1, x2, y2, z2):                              # 두 점 사이의 거리 계산
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** (1/2)


minlen = 1e9
lenSC = calculate(ax, ay, az, cx, cy, cz)
lenEC = calculate(bx, by, bz, cx, cy, cz)

while 1:
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    mz = (az + bz) / 2
    lenKC = calculate(mx, my, mz, cx, cy, cz)           # mid(임의의 점)과 C 사이의 거리
    if abs(minlen - lenKC) <= 1e-6:
        print('{:.10f}'.format(lenKC))
        break
    minlen = min(lenKC, minlen)
    if lenSC < lenEC:               # [시작점과 C 사이의 거리]가 [끝점과 C 사이의 거리]보다 작을때, 끝점을 시작점쪽으로 당기기
        bx, by, bz = mx, my, mz
        lenEC = lenKC
    else:
        ax, ay, az = mx, my, mz
        lenSC = lenKC

# import math
# import sys
#
# ax, ay, az, bx, by, bz, cx, cy, cz = map(int, sys.stdin.readline().split())
#
#
# def calculate(x1, y1, z1, x2, y2, z2):                              # 두 점 사이의 거리 계산
#     #return math.sqrt(( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 ))
#     return ( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 ) **(1/2)
#
# start = [ax, ay, az]
# end = [bx, by, bz]
# mid = [0, 0, 0]
# minlen = 1e9
#
# while 1:
#     mid[0] = (start[0] + end[0]) / 2
#     mid[1] = (start[1] + end[1]) / 2
#     mid[2] = (start[2] + end[2]) / 2
#     lenKC = calculate(mid[0], mid[1], mid[2], cx, cy, cz)           # mid(임의의 점)과 C 사이의 거리
#     lenSC = calculate(start[0], start[1], start[2], cx, cy, cz)
#     lenEC = calculate(end[0], end[1], end[2], cx, cy, cz)
#     if minlen == lenKC:
#         print('{:.10f}'.format(lenKC))
#         break
#     minlen = min(lenKC, minlen)
#     if lenSC < lenEC:               # [시작점과 C 사이의 거리]가 [끝점과 C 사이의 거리]보다 작을때, 끝점을 시작점쪽으로 당기기
#         end = mid[:]
#     else:
#         start = mid[:]
