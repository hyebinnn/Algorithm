# 사탕 게임

N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))
candy = 0

def check(board):
    cnt, c = 1, 1
    for i in range(N):
        c = 1
        for j in range(N-1):                            # 일렬로 행 탐색
            if board[i][j] == board[i][j+1]:
                c += 1
            else:
                c = 1
            cnt = max(cnt, c)
        c = 1
        for j in range(N-1):                            # 일렬로 열 탐색
            if board[j][i] == board[j+1][i]:
                c += 1
            else:
                c = 1
            cnt = max(cnt, c)

    return cnt


for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:                # 행이 다르다면
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            candy = max(candy, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]         # 원상복구
    for j in range(N-1):
        if board[j][i] != board[j+1][i]:                # 열이 다르다면
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            candy = max(candy, check(board))
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(candy)