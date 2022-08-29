# 포도주 시식

import sys
input = sys.stdin.readline

podo = [0]
n = int(input())
for _ in range(n):
    podo.append(int(input()))

dp = [0] * 10001
dp[1] = podo[1]
if n >= 2:
    dp[2] = podo[1] + podo[2]


if n >= 3:
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + podo[i], dp[i-3]+podo[i-1]+podo[i])


print(dp[n])