# 회의실 배정

# 그리디

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

cnt = 1
end = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= end:
        cnt += 1
        end = meeting[i][1]
print(cnt)








# dfs 이용 --> 시간초과 ㅜㅜ
# N = int(input())
# meeting = []
# for _ in range(N):
#     meeting.append(list(map(int, input().split())))
#
# meeting.sort()
# result = 0
#
# def dfs(end, cnt):
#     finish = 1
#     global result
#     for i in range(N):
#         if meeting[i][1] > (2**31-1):
#             break
#         if meeting[i][0] >= end:
#             finish = 0
#             dfs(meeting[i][1], cnt+1)
#     if finish:
#         result = max(result, cnt)
#
#
# for m in meeting:
#     if m[1] > (2**31-1):
#         break
#     dfs(m[1], 1)        # start, end, cnt
# print(result)
