# 단지번호 붙이기

from collections import deque

N = int(input())
space = []
for i in range(N):
    space.append(list(map(int, input())))
visited = [[False]*N for _ in range(N)]
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    count = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] == 1:
                    count += 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return count

danji = 0
while 1:
    bfs(0,0)

