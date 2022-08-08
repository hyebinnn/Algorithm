# 센서

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

dis = []
for i in range(1, n):
    dis.append(sensor[i]-sensor[i-1])

dis.sort()

print(sum(dis[:n-k] if n > k else 0))