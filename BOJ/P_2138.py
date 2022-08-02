# 전구와 스위치
# 다시...

n = int(input())
A = list(map(int, input()))
B = list(map(int, input()))

def switch(i):
    if i == 0:
        A[i], A[i+1] = abs(A[i] - 1), abs(A[i+1] - 1)       # 0 -> 1,  1 -> 0
    elif i == n-2:
        A[i], A[i+1] = abs(A[i] - 1), abs(A[i+1] - 1)
    elif i == n-1:
        A[i]  = abs(A[i] - 1)
    else:
        A[i], A[i+1], A[i+2] = abs(A[i] - 1), abs(A[i+1] - 1), abs(A[i+2] - 1)


# zip (tuple) 로 반환
cnt = 0
for index, (a, b) in enumerate(zip(A, B)):
    if a != b:
        switch(index)
        cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)

