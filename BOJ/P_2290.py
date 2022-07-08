# LCD Test

s, n = map(int, input().split())
w = s + 2
h = 2 * s + 3


# 0
def zero():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:  # 처음과 마지막이 아니라면 (그 사이)
            num[0][i] = '-'
    for i in range(w):
        if i != 0 and i != w - 1:  # 처음과 마지막이 아니라면 (그 사이)
            num[-1][i] = '-'
    for j in range(h):
        if j % (s + 1):  # s=2) 3의 배수일 때, 빈칸임
            num[j][-1] = '|'
            num[j][0] = '|'

    return list(map(lambda x: ''.join(x) + ' ', num))

def one():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(h):
        if i % (s + 1):
            num[i][-1] = '|'
    return list(map(lambda x: ''.join(x) + ' ', num))

def two():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
            num[-1][i] = '-'
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1) and i < (s * 2 - 1):
            num[i][-1] = '|'
        elif i % (s + 1) and i > (s * 2 - 1):
            num[i][0] = '|'
    return list(map(lambda x: ''.join(x) + ' ', num))

def three():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
            num[-1][i] = '-'
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1):
            num[i][-1] = '|'
    return list(map(lambda x: ''.join(x) + ' ', num))

def four():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1) and i < (s * 2 - 1):
            num[i][-1] = '|'
            num[i][0] = '|'
        elif i % (s + 1) and i > (s * 2 - 1):
            num[i][-1] = '|'

    return list(map(lambda x: ''.join(x) + ' ', num))

def five():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
            num[-1][i] = '-'
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1) and i < (s * 2 - 1):
            num[i][0] = '|'
        elif i % (s + 1) and i > (s * 2 - 1):
            num[i][-1] = '|'
    return list(map(lambda x: ''.join(x) + ' ', num))

def six():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
            num[-1][i] = '-'
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1) and i < (s * 2 - 1):
            num[i][0] = '|'
        elif i % (s + 1) and i > (s * 2 - 1):
            num[i][0] = '|'
            num[i][-1] = '|'
    return list(map(lambda x: ''.join(x) + ' ', num))

def seven():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
    for i in range(h):
        if i % (s + 1):
            num[i][-1] = '|'
    return list(map(lambda x:''.join(x) + ' ', num))


def eight():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
            num[-1][i] = '-'
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1) and i < (s * 2 - 1):
            num[i][0] = '|'
            num[i][-1] = '|'
        elif i % (s + 1) and i > (s * 2 - 1):
            num[i][0] = '|'
            num[i][-1] = '|'
    return list(map(lambda x:''.join(x) + ' ', num))


def nine():
    num = [[' ' for _ in range(w)] for _ in range(h)]
    for i in range(w):
        if i != 0 and i != w - 1:
            num[0][i] = '-'
            num[-1][i] = '-'
            num[s * 2 - 1][i] = '-'
    for i in range(h):
        if i % (s + 1) and i < (s * 2 - 1):
            num[i][0] = '|'
            num[i][-1] = '|'
        elif i % (s + 1) and i > (s * 2 - 1):
            num[i][-1] = '|'
    print(num)
    return list(map(lambda x:''.join(x) + ' ', num))


numbers = str(n)
result = []
for i in range(len(numbers)):
    if int(numbers[i]) == 1:
        result.append(one())
    elif int(numbers[i]) == 2:
        result.append(two())
    elif int(numbers[i]) == 3:
        result.append(three())
    elif int(numbers[i]) == 4:
        result.append(four())
    elif int(numbers[i]) == 5:
        result.append(five())
    elif int(numbers[i]) == 6:
        result.append(six())
    elif int(numbers[i]) == 7:
        result.append(seven())
    elif int(numbers[i]) == 8:
        result.append(eight())
    elif int(numbers[i]) == 9:
        result.append(nine())
    elif int(numbers[i]) == 0:
        result.append(zero())

for e in map(lambda x: ''.join(x), zip(*result)):
    print(e)

    # --------------------------------- memo

    # n = [[' ', '-', '-', ' '], ['|', ' ', ' ', '|'], ['|', ' ', ' ', '|'], [' ', '-', '-', ' '], [' ', ' ', ' ', '|'], [' ', ' ', ' ', '|'], [' ', '-', '-', ' ']]
    # aa = []
    # aa.append(list(map(lambda x:''.join(x) + ' ', n)))
    #
    # aa.append(list(map(lambda x:''.join(x) + ' ', n)))
    # # [] 안의 원소들 공백없이 붙여주고, 각각 [], [] 끼리는 + ' ' (공백) 붙여줘서 1차원 리스트로 변경
    # # 출력값 = [' --  ', '|  | ', '|  | ', ' --  ', '   | ', '   | ', ' --  ']
    #
    # # for e in map(lambda x: ''.join(x), aa):              # 이건 큰 원소 안의 작은 원소들이 join 되고 큰 원소 2개 (9, 9) 는 각각 \n돼서 출력됨
    # #     print(e)
    #
    # for e in map(lambda x: ''.join(x), zip(*aa)):
    #     print(e)

    # # aa의 큰 원소들 2개 ( [' --  ', '|  | ', '|  | ', ' --  ', '   | ', '   | ', ' --  '],   [' --  ', '|  | ', '|  | ', ' --  ', '   | ', '   | ', ' --  '] )
    # # 이 2개를 join해줘서 9 9 나오도록 붙여준것
    # # 큰 원소 안의 '작은 원소들' 여러개 [' --  ', '|  | ', '|  | ', ' --  ', '   | ', '   | ', ' --  ']는 join 안하고 반복문으로 원소 빼내므로 \n 적용됨
    # # 그래서 예쁜 9 숫자가 만들어지는 것임.