# 상어 초등학교

n = int(input())
space = [[0]*n for _ in range(n)]            # 교실 공간
like = dict()                               # 각 학생의 좋아하는 학생들 번호
for _ in range(n**2):
    temp = list(map(int, input().split()))
    like[temp[0]] = temp[1:]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 현 좌석 주변에 있는 학생 수, 빈칸 수 return
def check_near(x, y):
    near = []
    empty = 0
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            if space[nx][ny] > 0:               # 주변에 있는 학생들 // 현 좌석 주변 모든 좌석이 현 학생이 좋아하는 학생인지 다 탐색한다면 시간초과 예상. -> 일단 주변에 있는 학생들만 모아두고 나중에 확인하자
                near.append(space[nx][ny])      # 주변 학생의 번호
            if space[nx][ny] == 0:
                empty += 1

    return near, empty

def satisfy(x, y, st):
    cnt = 0
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            if space[nx][ny] in like[st]:
                cnt += 1
    return cnt


satis = {0: 0, 1:1, 2:10, 3:100, 4:1000}
satisfaction = 0

for student in like:                # 자리를 선택할 학생 1명씩 (like의 키값들 전부 순회)
    arr = []
    for i in range(n):
        for j in range(n):
            like_cnt = 0
            if space[i][j] != 0:
                continue
            near, empty = check_near(i, j)
            for who in like[student]:
                if who in near:
                    like_cnt += 1
            tmp = [like_cnt, empty, i, j]       # 현 좌석의 주변 좋아하는 학생 수, 빈칸 수, 현 좌석 좌표
            arr.append(tmp)
    arr = sorted(arr, key = lambda x: (-x[0], -x[1], x[2], x[3]))
    x, y = arr[0][2], arr[0][3]          # 선택된 자리의 좌표값
    space[x][y] = student

for i in range(n):
    for j in range(n):
        cnt = satisfy(i, j, space[i][j])
        satisfaction += satis[cnt]

print(satisfaction)

