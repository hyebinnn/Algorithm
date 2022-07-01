# 맥주 마시면서 걸어가기
from collections import deque

t = int(input())        # 테스트 케이스 개수
result = []             # 최종 출력값

def gotoFestival(hx, hy, store, fx, fy):
    queue = deque()
    dx = [1, -1, 0, 0]          # 1 = 50m
    dy = [0, 0, 1, -1]
    sx, sy = [], []
    for i in range(n):
        sx.append(store[i][0])
        sy.append(store[i][1])
    # print('sx: ', sx)
    # print('sy: ', sy)
    total_dis = abs(fx - hx) + abs(fy - hy)  # festival과 home 간의 거리 = 총 필요한 beer 수
    if total_dis <= 20:
        return 'happy'  # 편의점 들리지 않고 바로 축제로 갈 수 있는 경우
    else:
        xx, yy = hx, hy
        queue.append((xx, yy))
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(drink) and 0 <= ny < len(drink[0]) and not visited[nx][ny]:
                    drink[nx][ny] = drink[x][y] - 1                 # 맥주 1병씩 drink
                    # print('nx, ny: ', (nx, ny))
                    # print('beer: ', drink[nx][ny])
                    if n!=0:
                        for j in range(n):
                            if (nx, ny) == (sx[j], sy[j]) and drink[nx][ny] >= 0:       # 편의점 무사히 도착
                                drink[nx][ny] = 20
                    # if (nx, ny) == (sx, sy) and drink[nx][ny] >= 0:          # 편의점 무사히 도착
                    #     drink[nx][ny] = 20
                    if drink[nx][ny] > 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

        if drink[fx][fy] == -1:
            return 'sad'
        else:
            return 'happy'
        # print('총 갯수: ', drink[fx][fy])


for _ in range(t):
    store = []
    n = int(input())  # 편의점 개수
    hx, hy = map(int, input().split())
    max_sx, max_sy = 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        max_sx, max_sy = max(max_sx, a//50), max(max_sy, b//50)             # space 면적 알기 위해 편의점 위치의 가장 긴 가로 세로 구하기
        store.append((a//50, b//50))
    fx, fy = map(int, input().split())
    fx, fy = fx//50, fy//50
    spacelen = max(max_sx, fx)
    spacewid = max(max_sy, fy)
    drink = [[-1]*(spacewid+1) for _ in range(spacelen+1)]       # [[열] * 행]
    visited = [[False] * (spacewid + 1) for _ in range(spacelen + 1)]
    drink[hx][hy] = 20
    result.append(gotoFestival(hx, hy, store, fx, fy))

for p in result:
    print(p)
