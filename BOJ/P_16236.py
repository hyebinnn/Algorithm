# 아기 상어

from collections import deque

N = int(input())
space = []
shark_size = 2
dx = [-1, 1, 0, 0]         # 상하
dy = [0, 0, -1, 1]         # 좌우

for i in range(N):
    a = list(map(int, input().split()))
    space.append(a)
    if 9 in a:
        x = i
        y = a.index(9)


def bfs(x, y):
    global shark_size
    dist = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    sequence = []                                  # 이동거리가 같은 물고기가 여럿일 때, 순서 정해주기 위한 리스트
    visited[x][y] = True                           # 현재 위치 방문
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny]:                         # 방문하지 않았다면
                if space[nx][ny] <= shark_size:             # 지나갈 수 있는 경우
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    if space[nx][ny] != 0 and space[nx][ny] < shark_size:           # 잡아먹는 경우
                        sequence.append((nx, ny, dist[nx][ny]))
                        # print('sequence: ',sequence)

    return sorted(sequence, key=lambda x: (-x[2], -x[0], -x[1]))                       # 잡아먹을 수 있는 물고기들 리스트
    # sorted의 key 인자에 함수를 넘겨주면 우선순위(정렬)가 정해짐
    # - 를 붙이면, 내림차순(reverse)으로 정렬
    # x[2]를 우선으로 내림차순 정렬, x[2]의 원소가 같은 경우에는 x[0] 부분을 비교해 내림차순으로 정렬
    # 문제상 우선순위 조건) 1. 거리 가까운 물고기   2. 위에 있는 물고기(x),  3. 가장 왼쪽 물고기(y)
    # 내림차순으로 정렬함으로써, 뒤에서부터 거리가 가깝고 위에 있는 순으로 리스트가 정렬됨.

t = 0            # 이동 소요 시간(출력값)
count = 0        # 잡아먹은 물고기 수
while 1:
    # print('bfs turn')
    s = bfs(x, y)

    # 더이상 먹을 물고기 없을 시, 엄마에게 도움 요청
    if len(s) == 0:
        break

    # 먹을 순서 정해진 물고기들
    nx, ny, dist = s.pop()          # 리스트의 맨마지막 요소 출력 -> 우선순위대로 뽑혀나옴

    t += dist
    space[x][y], space[nx][ny] = 0, 0
    x, y = nx, ny
    count += 1
    if count == shark_size:  # 잡아먹은 물고기 수 = 상어 크기일 때 상어 크기 +1
        shark_size += 1
        count = 0


print(t)

