# RGB 거리

n = int(input())
prices = [[0]]
dp = [[0] * 3 for _ in range(10001)]

for _ in range(n):
    prices.append(list(map(int, input().split())))

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + prices[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + prices[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + prices[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))