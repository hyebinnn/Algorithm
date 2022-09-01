# 컨베이어 벨트 위의 로봇

# 내구도가 0인 칸의 갯수가 k개 이상이면 종료
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))         # 각 칸의 내구도 (2N개의 칸)
robot = [False] * (N*2)

def rotate(step):
    while 1:
        step += 1
        final, f_robot = a.pop(), robot.pop()
        a.insert(0, final)
        robot.insert(0, f_robot)

        # print(f'step 1 a: {a}')
        # print(f'step 1 robot: {robot}')

        if robot[N-1] == True:
            robot[N-1] = False

        #step += 1
        for i in range(N-2, -1, -1):          # 2번 스텝
            if robot[i] == True and robot[i+1] == False and a[i+1] >= 1:
                robot[i], robot[i+1] = False, True
                a[i+1] -= 1
            if robot[N - 1] == True:
                robot[N - 1] = False
        # print(f'step 2 a: {a}')
        # print(f'step 2 robot: {robot}')

        if a.count(0) >= K:
            break

        #step += 1
        if a[0] != 0:           # 3번 스텝
            robot[0] = True
            a[0] -= 1
            # 로봇 올림

        # print(f'step 3 a: {a}')
        # print(f'step 3 robot: {robot}')

        #step += 1
        if a.count(0) >= K:
            break

    return step

#    rotate(step)

print(rotate(0))