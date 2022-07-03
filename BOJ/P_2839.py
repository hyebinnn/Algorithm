# 설탕 배달

n = int(input())            # 설탕 배달 양
p = 0                       # 봉지 수

while n >= 0:
    if n % 5 == 0:          # 5로 나누어 떨어질 때 , 3으로만 나누어져 n = 0일때도 이 if문은 참이 되어 p 출력 (0을 5로 나누어도 나머지는 0이니까)
        p += n // 5
        print(p)
        break
    n -= 3
    p += 1
if n < 0:
    print(-1)