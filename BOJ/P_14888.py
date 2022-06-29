N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

minvalue = 1e9          # 10억
maxvalue = -1e9
eq = 0

def dfs(i , r):
    global add, sub, mul, div, minvalue, maxvalue, eq
    if i == N:
        maxvalue = max(maxvalue, r)
        minvalue = min(minvalue, r)
    if add > 0:
        add -= 1
        eq = r + A[i]
        dfs(i+1, eq)
        add += 1
    if sub > 0:
        sub -= 1
        eq = r - A[i]
        dfs(i+1, eq)
        sub += 1
    if mul > 0:
        mul -= 1
        eq = r * A[i]
        dfs(i+1, eq)
        mul += 1
    if div > 0:
        div -= 1
        eq = int(r / A[i])
        dfs(i+1, eq)
        div += 1

# dfs 재귀호출이 풀리면서 랜덤으로 연산자의 +1이 되고 해당 dfs에서 마지막으로 돌린 if문에서 다시 쭉 뒷코드를
# 읽어나가기 때문에 랜덤으로 연산자 순서가 뒤바뀌게 되는것


dfs(1, A[0])

print(maxvalue)
print(minvalue)