# 빗물

h, w = map(int, input().split())
height = list(map(int, input().split()))

res, left_max, right_max = 0, -1, -1

for i in range(1, w-1):
    left_max, right_max = -1, -1
    for j in range(0, i):
        if height[j] < height[i]:       # 왼쪽 값들이 현재값보다 작으면 pass
            continue
        left_max = max(left_max, height[j])
    for k in range(i+1, w):
        if height[k] < height[i]:       # 왼쪽 값들이 현재값보다 작으면 pass
            continue
        right_max = max(right_max, height[k])
    if right_max != -1 and left_max != -1:
        filling = min(right_max, left_max)
        res += (filling - height[i])

print(res)





# def calculate(i, j):
#     cnt = 0
#     m = min(height[i], height[j])
#     for x in range(i+1, j):
#         cnt += (m-height[x])            # 물 고이는 구간 연산

#     return cnt

# long_h = 0
# long_index = -1
# res = 0
# morelong_index = -1

# for i in range(w-1):
#     if height[i] > height[i+1]:         # 하향
#         if morelong_index != -1 and long_index != -1:
#             res += calculate(long_index, morelong_index)
#             long_h = height[morelong_index]
#             long_index = morelong_index
#         if height[i] > long_h:
#             long_h = height[i]
#             long_index = i
#     elif height[i] < height[i+1]:      # 상향
#         morelong_index = i+1
#         if i+1 == w-1:             # 하향하지 않고 마지막 index
#             if long_index != -1:
#                 res += calculate(long_index, morelong_index)
# print(res)