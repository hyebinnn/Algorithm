# 바이러스
# dfs

import sys

C = int(sys.stdin.readline())
N = int(sys.stdin.readline())

ComList = []              # 컴퓨터 네트워크 쌍
d = [1]                   # 방문한 컴퓨터 번호
count = 0

def dfs(v):
    global count
    for x,y in ComList:
        if x == v:
            if y not in d:
                count += 1                # 바이러스 걸린 컴퓨터 카운트
                d.append(y)               # 2 삽입 (방문)
                dfs(y)

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    ComList.append(tmp)
    ComList.append(list(reversed(tmp)))                          # 1 2 / 2 3 / 5 3  인 경우, 마지막에 3번도 바이러스인데 input에 [0]번 인덱스만 들어가면, 5번 컴퓨터 바이러스라고 인식 못함.
                                                                # 거꾸로 2 1 / 3 2 / 3 5 버전도 input으로 넣어줘야 전체적으로 찾아낼 수 있다.


dfs(1)

print(count)