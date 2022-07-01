# 잃어버린 괄호

import re

# nums = re.split(r'([+,-])', input())

a = input().split('-')
print(a)

nums=[]
for i in a:
    result = 0
    s = i.split('+')
    print(s)
    for j in s:
        result += int(j)
    nums.append(result)
n = nums[0]
for i in range(1, len(nums)):
    n -= nums[i]

print(n)