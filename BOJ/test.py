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
# from itertools import combinations
#
# s = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
# blank = []
# for i in range(len(s)):
#     for j in range(len(s[0])):
#         if s[i][j] == 0:
#             blank.append([i, j])
# for combi in list(combinations(blank, 3)):
#     print(combi)
#

# from itertools import permutations
# from itertools import product
#
# items = [['a', 'b', 'c'], ['1', '3', '4', '5'], ['%', '@', '!!']]
# ss = ['+','+','-','*','/']
# print(len(list(permutations(ss, len(ss)))))
#
# print(int(-13/2))

a = [3,5,2,6,7,9,6,3,2]
a.sort()
print(a)
a = [a[:3], a[4:]]
a =
print(a)