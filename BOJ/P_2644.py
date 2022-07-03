# 촌수계산

N = int(input())
a, b = map(int, input().split())            # 계산해야하는 두 사람의 번호
M = int(input())
relation = [[] for _ in range(N+1)]         # 엮여있는 노드 저장하는 2차원 배열
visited = [False] * (N+1)
result = []

for _ in range(M):
    x, y = map(int, input().split())
    relation[x].append(y)       # 자식
    relation[y].append(x)       # 부모

def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in relation[v]:
        if not visited[i]:
            dfs(i, num)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)