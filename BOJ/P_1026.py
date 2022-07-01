# 보물

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

sortA = sorted(A)     # 1 1 3
sortB = sorted(B, reverse=True)                # 내림차순으로 정렬된 B // 30 20 10
BB = B.copy()

for i in range(n):
    max = sortB[i]         # 30
    max_index = BB.index(max)       # 30이 가지는 B에서의 index = 1
    BB[max_index] = -1              # 한번 거친 원소는 -1로 변경 (중복원소의 경우 index 찾을 때 최소 index밖에 안뜨는 것을 방지)
    print(BB)
    A[max_index] = sortA[i]
 
for i in range(n):
    S += A[i] * B[i]

print(S)
print(A)
print(B)