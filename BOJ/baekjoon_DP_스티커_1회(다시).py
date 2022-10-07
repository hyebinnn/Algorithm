# 스티커 9465

'''
from collections import deque

t = int(input())
d = [(1,0),(0,1),(-1,0),(0,-1)]


def run(sticker, n):
    queue = deque()
    dp = [[0] * n for _ in range(2)]
    take = [[True] * n for _ in range(2)]
    for i in range(2):
        for j in range(n):
            queue.append((i, j))

    while queue:  
        x, y = queue.popleft()         
        ans = True 
        for x in range(4):
            nx, ny = x + d[x][0], y + d[x][1]
            if nx < 0 or nx > 2 or ny < 0 or ny > n:
                continue
            if sticker[x][y] < sticker[nx][ny]:
                ans = False




for _ in range(t):
    n = int(input())
    sticker = []
    #dp = [[0] * n for _ in range(2)]
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
#    run(sticker, n)

'''




t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))