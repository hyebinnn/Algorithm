# num = [1, 2]
# fruits = ['apple', 'banana']
# color = ['red', 'yellow']
# print(list(zip(num, fruits, color)))
#
# def solution(brown, yellow):
#     answer = []
#     arr = []                # 약수 들어가있는 리스트
#     brown = brown - 4
#     if yellow == 1:  answer = [3, 3]
#     else:
#         for x in range(1, yellow+1):
#             if yellow % x == 0:
#                 arr.append(x)
#         for i in range(len(arr) // 2):
#             h = arr[i]
#             w = arr[-(i+1)]
#             result = w*2 + h*2
#             if result == brown:
#                 answer = [w+2, h+2]
#                 break
#     return answer
from collections import Counter

s = {4: [1,3], 3: [1, 9, 4, 5], 9: [8, 1, 2, 3], 8: [1, 9, 3, 4], 7: [2, 3, 4, 8], 1: [9, 2, 5, 7], 6: [5, 2, 3, 4], 5: [1, 9, 2, 8], 2: [9, 3, 1, 4]}
a = [(0,1), (0,0), (0,1), (2,4), (0,0), (3,6)]
print(s[4][1])