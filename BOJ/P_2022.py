# 사다리

x, y, c = map(float, input().split())
high = min(x, y)
low = 0
result = 0

while low + 0.001 <= high:
    w = (low + high) / 2                # mid
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    guess_c = (h1*h2) / (h1+h2)
    if guess_c >= c:                    # 주어진 c보다 길다면 (=건물사이 k는 짧음)
        result = w
        low = w                         # k 늘리기
    else:
        high = w                        # k 짧게 하기

print(result)

