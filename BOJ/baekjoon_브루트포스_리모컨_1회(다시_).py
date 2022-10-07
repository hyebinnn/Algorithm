# 1107번

now_ch = 100
N = int(input())
M = int(input())
broken = list(map(int, input().split()))
result = []
new_ch = []

def dfs(channel, broke):
    for i in range(len(channel)):
        ch = channel[i]
        while (ch in broke) and (ch != 0):
            ch -= 1
        new_ch.append(ch)

        


if now_ch == N:
    print(0)
else:
    listN = list(str(N))
    dfs(listN, broken)
