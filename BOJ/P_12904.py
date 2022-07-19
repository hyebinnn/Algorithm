# A와 B

s = input()
t = input()


while len(t) != len(s):
    if t[-1] == 'A':
        t = t[:-1]            # 마지막 원소 제거
    elif t[-1] == 'B':
        t = t[:-1]            # 마지막 원소 제거
        t = ''.join(reversed(t))

print(1 if s == t else 0)










# def check(x):
#     re_x = ''.join(reversed(x))
#     if x+'A' in t:
#         return x+'A'
#     elif re_x+'B' in t:
#         return re_x+'B'
#     elif re_x+'B' not in t:
#         return check(re_x+'B')
#     else:
#         return 0
#
#
#
# while len(s) != len(t):
#     s = check(s)
#     if s == 0:
#         print(s)
#         break
#     print(s)
#
# if s == t:
#     print('s:', s)
#     print('t:', t)
#     print(1)