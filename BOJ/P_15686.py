# 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
city = []
chicken = []  # 모든 치킨집 좌표들
home = []  # 모든 집 좌표들

for _ in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))
            city[i][j] = 0
        elif city[i][j] == 1:
            home.append((i, j))


def C_distance(chickens):           # 도시의 치킨 거리 계산
    ans = 0
    for h in home:
        min_dis = 1e9
        for c in chickens:          # M번 for문
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_dis = min(min_dis, dis)
        ans += min_dis              # 한 집의 최소 치킨 거리를 더해준다 --> 모든 집의 최소 치킨 거리를 더한 값이 도시의 치킨 거리

    return ans


result = 1e9

for ch in list(combinations(chicken, m)):  # 폐업 안 시키고 유지할 m개씩 조합
    city_chicken = C_distance(ch)
    result = min(result, city_chicken)

print(result)
