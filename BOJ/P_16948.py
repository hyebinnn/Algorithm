# 데스 나이트
from pprint import pprint
from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, 2, -2, -1, 1]


def bfs(x, y):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    moving = [[0] * N for _ in range(N)]             # 이동 횟수
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                moving[nx][ny] = moving[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
                if (nx, ny) == (r2, c2):
                    return moving[nx][ny]
            # print("visited")
            # pprint(visited)
            # print("moving")
            # pprint(moving)

    return 0

if bfs(r1, c1) == 0:
    print(-1)
else:
    print(bfs(r1, c1))


# ----------------------------------------------------

# N = int(input())
# r1, c1, r2, c2 = map(int, input().split())
# chess = [[-1]*N for _ in range(N)]              # 방문 및 거리 측정
#
# d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     chess[x][y] = 0
#     while queue:
#         x, y = queue.popleft()
#         for dx, dy in d:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < N and 0 <= ny < N and chess[nx][ny] == -1:
#                 chess[nx][ny] = chess[x][y] + 1
#                 queue.append((nx, ny))
#
# bfs(r1, c1)
# print(chess[r2][c2])