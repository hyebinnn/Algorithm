# pypy3 성공
# python 시간초과

from collections import deque
import sys

n, l, r = map(int, sys.stdin.readline().split())
country = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(n):
    country.append(list(map(int, sys.stdin.readline().split())))


def findNear(x, y):
    q = deque()
    q.append((x, y))
    vv[x][y] = True
    arr = [(x, y)]                    # 연합 국가 수
    people = country[x][y]            # 연합 인구수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n and not vv[nx][ny]:
                if l <= abs(country[x][y] - country[nx][ny]) <= r:
                    q.append((nx, ny))
                    arr.append((nx, ny))
                    people += country[nx][ny]
                    vv[nx][ny] = True
    for i, j in arr:
        country[i][j] = int(people / len(arr))

    return len(arr)


day = 0
while 1:
    finish = True
    vv = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not vv[i][j]:                # 연합이 여러 개일때, 한 연합파트 먼저 탐색 후 방문 안했던 다른 연합 찾아내기
                if findNear(i, j) > 1:
                    finish = False

    if finish:
        print(day)
        break
    day += 1
