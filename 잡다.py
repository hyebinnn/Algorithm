# import copy
# A = [[10], [30,20], [22]]
# #B = copy.deepcopy(A)
# B = [x[:] for x in A]
# B[1][0] = 40
#
# print(B)
# print(A)

s = [[6, 8, 2, 6, 2],
 [3, 2, 3, 4, 6],
 [6, 7, 3, 3, 2],
 [7, 2, 5, 3, 6],
 [8, 9, 5, 2, 7]]

for i in len(s):
    for j in len(s[0]):
        print(i)
        print(j)