# 제곱수의 합

from math import sqrt


n = int(input())
dp = [1e4] * (n+1)

dp[0]= 0

square_root = int(sqrt(n))

for root in range(1, square_root+1):
    for j in range(root**2, n+1):
        dp[j] = min(dp[j-root**2]+1, dp[j])


print(dp[n])

'''
print(int(sqrt(98989)))
for i in range(1, n+1):
    square_root = int(sqrt(i))
    for j in range(1, square_root+1):
        dp[i] = min(dp[i], dp[i-(j**2)] + 1)

print(dp[n])
'''
