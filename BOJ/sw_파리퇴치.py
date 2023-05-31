
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    space = []
    for x in range(N):
        space.append(list(map(int, input().split())))

    max_res = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            res = 0
            for i in range(M):
                for j in range(M):
                    res += space[x+i][y+j]
            max_res = max(res, max_res)
    
    print(f'#{test_case} {max_res}')