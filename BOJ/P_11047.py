# 동전 0

n, k = map(int, input().split())
coins = []
p = 0                   # 필요 동전 개수

for _ in range(n):
    a = int(input())
    if a <= k:
        coins.append(a)        # k보다 작은 동전만 coins 리스트에 삽입

coins.sort(reverse=True)

i = 0

while k > 0:
    p += k // coins[i]
    k = k % coins[i]
    i += 1

print(p)
