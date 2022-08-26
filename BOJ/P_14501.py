# 퇴사

n = int(input())
work = [[0]]
dp = [0] * (n+2)
for i in range(n):
    work.append(list(map(int, input().split())))

for i in range(n, 0, -1):
    d, p = work[i][0], work[i][1]
    if i + d > n+1:             # deadline 초과
        dp[i] = dp[i+1]

    else:
        dp[i] = max(p+dp[i+d], dp[i+1])         # 현재 일하고 + 일하는데 걸리는 시간 뒤의 dp값  ||  현재 일 안하고 이전 값 복사

print(dp[1])



'''
dp = [0] * (n+2)

for i in range(1, n+1):
    t, p = work[i-1][0], work[i-1][1]
    if i + t > n+1:
        continue
    dp[i+t] = max(dp[i] + p, dp[i+t])

print(dp)

if dp[n+1] != 0:
    print(dp[n + 1])
else:
    print()'''