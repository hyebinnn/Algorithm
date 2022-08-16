# 쉬운 계단 수

n = int(input())
dp = [[0] * 10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for S in range(10):
        if S == 0:
            dp[i][S] = dp[i-1][S+1]
        elif S == 9:
            dp[i][S] = dp[i-1][S-1]
        else:
            dp[i][S] = dp[i-1][S+1] + dp[i-1][S-1]

print(sum(dp[n])%1000000000)