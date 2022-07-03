# 참외밭
# 1: 동쪽, 2: 서쪽, 3: 남쪽, 4: 북쪽

import sys

K = int(sys.stdin.readline())
field=[]
for i in range(6):
    field.append(list(map(int, input().split())))        # [4,50] = [변의 방향, 길이]

largeLen = 0
largeWid = 0
for i in range(6):
    if field[i][0] == 4 or field[i][0] == 3:
        largeLen = max(largeLen, field[i][1])
        # if lm < field[i][1]: lm = field[i][1]
        # largeLen = lm                                # 큰 사각형 (가장 긴 세로 변)
    else:
        largeWid = max(largeWid, field[i][1])
        # if wm < field[i][1]: wm = field[i][1]
        # largeWid = wm                                # 가장 긴 가로 변

bigSquare = largeWid * largeLen
small = []

for i in range(6):                                         # 6개를 2개로 이어 붙여서 12개짜리로 만들어도 됨
    if i == 0:
        if field[-1][0] == field[i+1][0]:
            small.append(field[i][1])                       # 작은 사각형의 가로(세로)변
    elif i == 5:
        if field[i-1][0] == field[0][0]:
            small.append(field[i][1])                       # 작은 사각형의 가로(세로)변
    else:
        if field[i-1][0] == field[i+1][0]:
            small.append(field[i][1])                       # 작은 사각형의 가로(세로)변

smallSquare = 1
for i in small:
    smallSquare *= i

fieldArea = bigSquare - smallSquare
print(fieldArea * K)