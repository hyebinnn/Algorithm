from pprint import pprint
from collections import deque

T = int(input())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def check(x, y):
    # if space[x][y] != -1: count = 1
    # else: count = 0  # 근처 구역 count
    q = deque()
    q.append((x, y))
    check_visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < N and 0 <= ny < N and not check_visited[nx][ny]:
                if space[nx][ny] != -1:
                    q.append((nx, ny))
                    check_visited[nx][ny] = True


def sink(x, y, year):           # 잠기는 땅 -1로 변경
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    if space[x][y] <= year:
        space[x][y] = -1  # 물에 잠긴 표시
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] <= year:
                    space[nx][ny] = -1  # 물에 잠긴 표시
                visited[nx][ny] = True
                queue.append((nx, ny))

    # for i in range(len(space)):
    #     for j in range(len(space[0])):
    #         if space[i][j] != -1 and not check_visited[i][j]:
    #             check(i, j)
    #             spot += 1
    #
    # return spot

result = []

for _ in range(T):
    space = []
    max_spot = -1
    N = int(input())
    for i in range(N):
        space.append(list(map(int, input().split())))
    # visited = [[False] * N for _ in range(N)]                    # for sink
    check_visited = [[False] * N for _ in range(N)]              # for check
    for y in range(1, max(map(max, space)) + 1):
        visited = [[False] * N for _ in range(N)]                    # for sink
        check_visited = [[False] * N for _ in range(N)]  # for check
        spot = 0
        sink(0, 0, y)
        for i in range(N):
            for j in range(N):
                if space[i][j] != -1 and not check_visited[i][j]:
                    check(i, j)
                    spot += 1
        max_spot = max(max_spot, spot)

    result.append(max_spot)

for i, x in enumerate(result):
    print('#'+str(i+1), x)