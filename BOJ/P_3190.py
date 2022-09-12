# 뱀

from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
space = [[0] * n for _ in range(n)]
for _ in range(k):
    ax, ay = map(int, input().split())
    space[ax-1][ay-1] = '#'               # 사과 자리

L = int(input())
snake_dis = []
for _ in range(L):
    snake_dis.append(list(map(str, input().split())))

snake = deque()
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]          # 위, 오른쪽, 아래, 왼쪽

def game(x, y, d, t):                          # d = 0: 상, d = 1: 오른쪽, d = 2: 하, d = 3: 왼쪽
    queue = deque()
    snake.append((x, y))
    space[x][y] = 1
    queue.append((x, y, d, t))
    while queue:
        # pprint(space)   
        x, y, d, t= queue.popleft()
        for time, dir in snake_dis:
            time = int(time)
            if time == t and dir == 'L':                    # [1,0,3,2] 반복
                if d == 0:  d = 3
                else:
                    d -= 1
                snake_dis.pop(0)
                break
            elif time == t and dir == 'D':                  # [1,2,3,0] 반복
                if d == 3:  d = 0
                else:   d += 1
                snake_dis.pop(0)
                break


        # print(f't {t}, d {d}')


        nx, ny = x + direction[d][0], y + direction[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or space[nx][ny] == 1:          # 벽에 부딪힘
            return t+1        # 수정
        
        t += 1
        
        snake.append((nx, ny))      # snake 이동
        if space[nx][ny] == '#':
            space[nx][ny] = 1           # tail keep
            queue.append((nx, ny, d, t))
        else:    
            space[nx][ny] = 1        
            dx, dy = snake.popleft()                 # tail delete
            space[dx][dy] = 0
            queue.append((nx, ny, d, t))



print(game(0, 0, 1, 0))
        