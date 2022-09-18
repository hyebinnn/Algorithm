# 정수 삼각형

n = int(input())
triangle = []
dp = [[0] * i for i in range(1, n+1)]
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:          
            dp[i][j] = max(dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j])

print(max(dp[-1]))