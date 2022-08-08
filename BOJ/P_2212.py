# 센서

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

dis = []

if n == 1:
    res = 0
else:
    if k == 1:
        res = sensor[n-1] - sensor[0]
    else:
        for i in range(1, n):
            diff = sensor[i] - sensor[i-1]
            dis.append((diff, i-1, i))

        dis.sort(key=lambda x: (-x[0], x[1]))

        dis = dis[:k-1]         # 집중국 영역 나눌 부분 (k-1개) -> k개로 쪼개짐

        dis.sort(key=lambda x: x[1])
        print(dis)
        tmp = []
        tmp.append(sensor[:dis[0][1]+1])

        for i in range(1, len(dis)):
            tmp.append(sensor[dis[i-1][2]:dis[i][1]+1])

        tmp.append(sensor[dis[len(dis)-1][2]:])

        print(tmp)

        res = 0
        for x in tmp:
            if len(x) > 1:
                d = x[len(x)-1] - x[0]
                res += d
print(res)