# mine
# pypy3 통과, python 시간초과


from itertools import permutations
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
O_list = list(map(int, sys.stdin.readline().split()))
O_str = ['+', '-', '*', '/']
operator = []

max_ans = -1e9
min_ans = 1e9

for i in range(4):
    for num in range(O_list[i]):            # 각 연산자 몇개씩 주어졌는지
        operator.append(O_str[i])

operator = list(permutations(operator, sum(O_list)))            # 순서 상관있는 조합으로 전체 경우의 수 뽑아내기


def calculate(oper, ans, num2):                 # ans : 이전까지 연산한 값
    if oper == '+':
        r = ans + num2
    elif oper == '-':
        r = ans - num2
    elif oper == '*':
        r = ans * num2
    else:
        r = int(ans / num2)

    return r

for i in range(len(operator)):
    ans = A[0]
    for j in range(len(operator[0])):
        o = operator[i][j]
        ans = calculate(o, ans, A[j+1])
    max_ans = max(max_ans, ans)
    min_ans = min(min_ans, ans)

print(max_ans)
print(min_ans)