# 미로탐색
from collections import deque

N, M = map(int, input().split())
miro = []

for i in range(N):
        miro.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

def bfs(x, y):
    q.append((x,y))
    while q:
        nx, ny = q.popleft()                     # (0,0)
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]
            if xx < 0 or yy < 0 or xx >= N or yy >= M:                  # 범위를 벗어난다면
                continue
            if miro[xx][yy] == 0:                                       # 이동할 수 없다면
                continue
            if miro[xx][yy] == 1:                   # 첫방문인 경우
                miro[xx][yy] = miro[nx][ny] + 1                           # 기록 갱신 (방문했다면 1이 아님)
                q.append((xx, yy))                                  # 갈 수 있는 길 모두 큐에 삽입

    return miro[N-1][M-1]


print(bfs(0, 0))