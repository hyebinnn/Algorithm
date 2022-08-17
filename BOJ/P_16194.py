# 카드 구매하기 2

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [10000] * (n + 1)

dp[1] = p[1]

for i in range(2, n + 1):
    dp[i] = p[i]
    for k in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - k] + p[k])

print(dp[n])