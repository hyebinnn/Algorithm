from itertools import combinations
from itertools import product
from itertools import permutations


a = [1,2,3,4,5,6,7,8,9]
print(len(list(combinations(a, 2))))
print(len(list(permutations(a, 2))))
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        if abs(i-j) == 1:
            print((i, j))
            cnt += 1
print(cnt)