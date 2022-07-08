# 기타 레슨

N, M = map(int, input().split())                # 강의 수, 블루레이 개수
video = list(map(int, input().split()))         # 각 영상 길이

start = max(video)                               # 영상 중 가장 긴 길이 (1 블루레이 최소 크기)
end = sum(video)                                # 1 블루레이의 최대 크기
s = 0                                           # 각 영상 길이 더한 값
b_num = 0                                       # 블루레이 갯수
result = end

while start <= end:
    b_num = 0
    s = 0
    mid = (end + start) // 2                    # 임의로 가정할 블루레이 크기
    for x in video:
        if (s + x) > mid:                      # 블루레이의 크기를 넘어선다면
            b_num += 1                          # 블루레이 갯수 + 1
            s = 0
        s += x
    if s != 0:                                  # 블루레이 크기보다 작아서 1을 증가시키지 못한 경우
        b_num += 1
    if b_num > M:                               # 블루레이 크기 더 크게
        start = mid + 1
    else:                                       # 블루레이 갯수가 M과 같아도 크기를 더 작은 것을 찾는게 POINT!
        result = min(result, mid)
        end = mid - 1
print(result)

