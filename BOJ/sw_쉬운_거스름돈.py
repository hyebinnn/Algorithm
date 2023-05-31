T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    change = N
    for i in range(len(money_list)):
        if (change // money_list[i]) < 1:
            money_list[i] = 0
            continue
        ans = change // money_list[i]
        change = change - money_list[i] * ans
        money_list[i] = ans

    str_money_list = ' '.join(map(str, money_list))
    print(f'#{test_case} \n{str_money_list}')


