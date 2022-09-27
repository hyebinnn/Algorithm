# 이동하기

n, m = map(int, input().split())
candy = []
dp = [[0] * m for _ in range(n)]
for _ in range(n):
    candy.append(list(map(int, input().split())))

dp[0][0] = candy[0][0]
direction = [(1, 0), (0, 1), (1, 1)]

for i in range(n):
    for j in range(m):
        for dx, dy in direction:
            nx, ny = i-dx, j-dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            dp[i][j] = max(dp[i][j], dp[nx][ny]+candy[i][j])

print(dp[n-1][m-1])

