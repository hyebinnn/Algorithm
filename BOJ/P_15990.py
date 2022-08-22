# 1, 2, 3 더하기 5


T = int(input())

dp = [[0] * 3 for _ in range(100001)]
# 1, 2, 3으로 끝난 갯수 세기 (1, 2, 3) --> 3 = [1+2, 2+1, 3]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] = dp[i-1][1]% 1000000009 + dp[i-1][2]% 1000000009          # n이 5일때 합의 끝자리가 1로 끝나는 경우의 갯수
    dp[i][1] = dp[i-2][0]% 1000000009 + dp[i-2][2]% 1000000009
    dp[i][2] = dp[i-3][0]% 1000000009 + dp[i-3][1]% 1000000009


for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)

print(dp)