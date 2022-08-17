# 1로 만들기

n = int(input())
dp = [1e6] * (n+1)
dp[n] = 0


for x in range(n, 0, -1):
    if x % 3 == 0:
        dp[x // 3] = min(dp[x] + 1, dp[x//3])
    if x % 2 == 0:
        dp[x // 2] = min(dp[x] + 1, dp[x//2])
    dp[x-1] = min(dp[x] + 1, dp[x-1])

print(dp[1])