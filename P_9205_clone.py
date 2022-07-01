from collections import deque

t = int(input())

def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    print('sad')
    return

for i in range(t):
    n = int(input())  # 편의점 개수
    home = [int(x) for x in input().split()]
    store = []
    for j in range(n):
        x, y = map(int, input().split())
        store.append([x, y])
    fest = [int(x) for x in input().split()]
    visited = [False for i in range(n)]       # home 제외
    bfs()

