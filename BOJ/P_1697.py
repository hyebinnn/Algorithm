# 숨바꼭질

from collections import deque

n, k = map(int, input().split())
MAX = 10**5
dist = [0] * (MAX + 1)            # indexError 방지 -> MAX만큼 list 생성


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:                 # k보다 초과한 수에서 x-1 방법이 최소 시간이 걸리는 정답일 수도 있으니까 조건을 nx <= MAX로 설정
                dist[nx] = dist[x] + 1
                queue.append(nx)

bfs(n)
