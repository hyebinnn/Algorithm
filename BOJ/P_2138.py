# 전구와 스위치
from copy import deepcopy

n = int(input())
A = list(map(int, input()))
B = list(map(int, input()))
copyA = deepcopy(A)


def change(list, i):
    if i == 0:
        list[i], list[i+1] = abs(list[i]-1), abs(list[i+1]-1)
    elif i == n-1:
        list[i-1], list[i] = abs(list[i-1]-1), abs(list[i]-1)
    else:
        list[i-1], list[i], list[i+1] = abs(list[i-1]-1), abs(list[i]-1), abs(list[i+1]-1)


def switch_first():           # 맨 처음 전구 스위치 on 하는 경우
    cnt = 1
    change(A, 0)
    for i in range(1, n):
        if A[i - 1] != B[i - 1]:
            cnt += 1
            change(A, i)

    if A == B:
        return cnt
    else:
        return -1


def original_first():       # 맨 처음 전구 스위치 건드리지 않는 경우
    cnt = 0
    for i in range(1, n):
        if copyA[i - 1] != B[i - 1]:
            cnt += 1
            change(copyA, i)

    if copyA == B:
        return cnt
    else:
        return -1


res1 = switch_first()
res2 = original_first()

if res1 != -1 and res2 != -1:
    print(min(res1, res2))
elif res1 != -1 and res2 == -1:
    print(res1)
elif res2 != -1 and res1 == -1:
    print(res2)
else:
    print(-1)
