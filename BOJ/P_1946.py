# 신입 사원

import sys
import time

start = time.time()

T = int(sys.stdin.readline())        # 테스트 케이스 = 출력 갯수

for i in range(T):
    TL = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        TL.append(list(map(int, sys.stdin.readline().split())))           # 3 2 삽입

    TL.sort()
    passed = 1      # 서류심사 1등은 이미 채용, 면접 순위만 비교하면 됨
    m = TL[0][1]

    for j in range(1, N):
            if TL[j][1] < m:               # 서류 1등보다 면접 순위가 높다면
                m = TL[j][1]
                passed += 1
    print(passed)

print("time: ", time.time() - start)
