# 로봇청소기

from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())      # 좌표 및 방향 d
# 문제상) 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
direction = [0, 3, 2, 1, 0]         # direction[1] 의 왼쪽방향 direction[2]
space = []
dx = [-1, 0, 1, 0]                  # (-1, 0) 북쪽, (1, 0) 남, (0, -1) 서, (0, 1) 동 / 위치로 이동
dy = [0, 1, 0, -1]
# dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]        # 북 동 남 서 (문제상 방향 index 순으로)
visited = [[False]*M for _ in range(N)]
for i in range(N):
    space.append(list(map(int, input().split())))

def bfs(x, y, d):
    Continuous = 0
    clean = 1
    queue = deque()
    queue.append([x, y, d])
    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = True
        left_d = direction[direction.index(d) + 1]  # 현재 청소기 방향의 index + 1 = 현 방향의 왼쪽 방향
        nx = x + dx[left_d]                         # 왼쪽 방향으로 회전한 위치
        ny = y + dy[left_d]
        if 0 <= nx < N and 0 <= ny < M:
            if space[nx][ny] == 0 and not visited[nx][ny]:      # 왼쪽에 청소하지 않은 빈 공간이 있다면,
                queue.append([nx, ny, left_d])                  # 1칸 전진, 왼쪽 회전
                visited[nx][ny] = True
                clean += 1
                Continuous = 0
            else:
                Continuous += 1
                if Continuous == 4:
                    if left_d == 0:
                        behind_d = 2
                    elif left_d == 2:
                        behind_d = 0
                    elif left_d == 1:
                        behind_d = 3
                    elif left_d == 3:
                        behind_d = 1
                    nx, ny = x + dx[behind_d], y + dy[behind_d]
                    if space[nx][ny] == 1:  # 바로 뒤쪽이 벽이라면
                        return clean  # 작동을 멈춤
                    else:
                        queue.append([nx, ny, left_d])  # 바뀐 방향이 아닌 현 방향과 후진한 좌표값 queue에 삽입
                        Continuous = 0
                        visited[nx][ny] = True
                else:
                    queue.append([x, y, left_d])  # 왼쪽 또 회전

    return clean


print(bfs(r, c, d))