# 인구이동

from collections import deque

n, l, r = map(int, input().split())
country = []
near = [[False]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
near_visited = [[False] * n for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


for _ in range(n):
    country.append(list(map(int, input().split())))


def movement(x, y):             # 인구 이동
    cnt = 1            # 인접한 칸(연합)의 개수
    people = country[x][y]          # 연합 인구수
    arr = []                        # 인구 이동할 부분 좌표들만 모아두기
    queue = deque()
    queue.append((x, y))
    near_visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        arr.append((x, y))
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n and not near_visited[nx][ny]:
                if near[nx][ny]:
                    queue.append((nx, ny))
                    cnt += 1
                    people += country[nx][ny]
                near_visited[nx][ny] = True
    for i, j in arr:
        country[i][j] = int(people / cnt)


day = 0
def findNear(x, y):
    global day
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[x][y] - country[nx][ny]) <= r:
                    queue.append((nx, ny))
                    near[x][y], near[nx][ny] = True, True
                visited[nx][ny] = True


findNear(0,0)
for i in range(n):
    for j in range(n):
        if near[i][j]:          # 인접 부분만
            movement(i, j)

print(day)