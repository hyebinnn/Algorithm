# 달팽이

from pprint import pprint

N = int(input())
find_num = int(input())

deep = N // 2

snail = [[0]*N for _ in range(N)]
nums = [x for x in range(N**2, 0, -1)]
snail[N//2][N//2] = 1                   # 정가운데 좌표값은 무조건 1

result = []

for k in range(deep):
    for i in range(k, N-k):
        result.append((i, k))
    for i in range(k+1, N-k):
        result.append((N-k-1, i))
    for i in range(N-k-2, k-1, -1):
        result.append((i, N-k-1))
    for i in range(N-k-2, k, -1):
        result.append((k, i))



for x, y in enumerate(result):
    snail[y[0]][y[1]] = nums[x]
    if nums[x] == find_num:
        find_xy = (y[0]+1, y[1]+1)

if find_num == 1:   find_xy = (N//2+1, N//2+1)

for x in snail:
    print(*x, sep=' ')
print(*find_xy)
