# 가장 긴 증가하는 부분 수열 4

n = int(input())
a = list(map(int, input().split()))

dp = [[1, []] for _ in range(n+1)]
dp[0][1].append(a[0])


for i in range(1, n):
    max_i = -1
    for j in range(i):
        if a[j] < a[i]:
            if dp[j][0]+1 > dp[i][0]:
                dp[i][0] = dp[j][0] + 1
                max_i = j
    if max_i != -1:
        dp[i][1].extend(dp[max_i][1])
    dp[i][1].append(a[i])

#    print(dp)

print(max(dp)[0])
print(*max(dp)[1])