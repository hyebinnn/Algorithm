# 경쟁적 전염

# n, k = map(int, input().split())
# space = []
# for _ in range(n):
#     space.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
# d = [(1, 0),(-1, 0), (0, 1), (0, -1)]
# visited = [[0] * n for _ in range(n)]
#
#
# def bfs(x, y):                           # 바이러스 전염
#     visited[x][y] = 1
#     for i in range(4):
#         nx, ny = x + d[i][0], y + d[i][1]
#         if 0 <= nx < n and 0 <= ny < n and space[nx][ny] == 0 and not visited[nx][ny]:
#             visited[nx][ny] = 1
#             space[nx][ny] = space[x][y]
#
#
# virus = []
# virus_visited = [[0] * n for _ in range(n)]
# count = 0                        # 시간 (초)
# while count < s:
#     if all(0 not in l for l in space):              # 0이 하나도 존재하지 않는지 = 바이러스 all 전염 (s 무쓸모)
#         break
#     for i in range(n):
#         for j in range(n):
#             if space[i][j] != 0 and not virus_visited[i][j]:
#                 virus_visited[i][j] = 1             # 탐색 완료
#                 virus.append([i, j])
#
#     virus.sort(key = lambda x: space[x[0]][x[1]])               # 바이러스 숫자가 작은 순서대로 정렬 - x[0], x[1] 행 열 (x = 1차원 배열 원소)
#     for arr in virus:
#         bfs(arr[0], arr[1])
#     count += 1
#
# print(space[x-1][y-1])


from collections import deque

n, k = map(int, input().split())
space, virus = [], []
for xx in range(n):
    temp = list(map(int, input().split()))
    space.append(temp)
    for yy, value in enumerate(temp):
        if value != 0:
            virus.append((value, 0, xx, yy))           # 바이러스 넘버, 시간(초), 좌표값 x, y

queue = deque(sorted(virus))                        # 바이러스 넘버순으로 정렬

s, X, Y = map(int, input().split())
d = [(1, 0),(-1, 0), (0, 1), (0, -1)]

while queue:
    v, cnt, x, y = queue.popleft()
    if cnt == s:
        break
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n and space[nx][ny] == 0:
            space[nx][ny] = v
            queue.append((v, cnt + 1, nx, ny))

print(space[X-1][Y-1])
