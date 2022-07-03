# 셀프 넘버

dn = []
selfnum = []

for i in range(1, 10001):
    d = i
    for j in str(i):
        d += int(j)          # d는 생성자가 존재하므로 셀프 넘버 x
    dn.append(d)

    if i not in dn:
        selfnum.append(i)

print(*selfnum, sep='\n')