
# naver AI 부스트캠프 4기 자가진단_카펫

# mine
def solution(brown, yellow):
    answer = []
    arr = []  # 약수 들어가있는 리스트
    brown = brown - 4
    if yellow == 1:
        answer = [3, 3]
    else:
        for x in range(1, yellow + 1):
            if yellow % x == 0:
                arr.append(x)
            if x ** 2 == yellow:
                arr.append(x)

        for i in range(len(arr) // 2):
            h = arr[i]
            w = arr[-(i + 1)]
            result = w * 2 + h * 2
            if result == brown:
                answer = [w + 2, h + 2]
                break
    return answer



# someone
# def solution(brown, red):
#     nm = brown + red
#     for n in range(1, nm+1):
#         if nm%n != 0:
#             continue
#         m = nm//n
#         if (n-2)*(m-2) == red:
#             return sorted([n, m], reverse = True)
#
