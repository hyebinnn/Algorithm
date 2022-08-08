# 센서

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
#sensor = list(set(sensor))          # 중복 x, 정렬 완료

dis = []

for i in range(1, n):
    diff = sensor[i] - sensor[i-1]
#    dis.append((diff, sensor[i-1], sensor[i]))
    dis.append((diff, i-1, i))

dis.sort(key=lambda x: (-x[0], x[1]))
print(dis)

for i in range(len(dis) - (k-1)):
    dis.pop()

dis.sort(key=lambda x: x[1])

tmp = []
tmp.append(sensor[:dis[0][1]+1])
for i in range(1, len(dis)):
    tmp.append(sensor[dis[i-1][2]:dis[i][1]+1])
    if i == len(dis)-1:
        tmp.append(sensor[dis[i][2]:])


print(tmp)
res = 0
for x in tmp:
    if len(x) > 1:
        d = x[len(x)-1] - x[0]
        res += d
print(res)