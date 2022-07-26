# 연구소

from collections import deque
import sys
import copy

n, m = map(int, sys.stdin.readline().split())
space = []
for _ in range(n):
    space.append(list(map(int, sys.stdin.readline().split())))
print(space)
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_safe = 0


def bfs():  # 전염
    global max_safe
    # result = 0
    ans = copy.deepcopy(space)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if ans[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m and ans[nx][ny] == 0:
                ans[nx][ny] = 2
                queue.append((nx, ny))

    result = checkSafe(ans)
    # for i in range(n):
    #     result += ans[i].count(0)             # count는 시간 오래 걸림
    max_safe = max(result, max_safe)


def checkSafe(ans):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ans[i][j] == 0:
                cnt += 1
    return cnt


def wall(cnt):                   # backTracking (백트래킹) 벽 세우기
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if space[i][j] == 0:
                space[i][j] = 1  # 벽 세움
                wall(cnt + 1)
                space[i][j] = 0  # 다시 허문다


wall(0)

print(max_safe)
