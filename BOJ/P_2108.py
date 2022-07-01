# 통계학

import sys
from collections import Counter        # 개수 세는 라이브러리 (dictionary 대신 이거 쓰면 코드 간결해짐)

N = int(sys.stdin.readline())
nums = []
dict = {}

for _ in range(N):
    n = int(sys.stdin.readline())
    nums.append(n)
    if n not in dict:
        dict[n] = 1

n = len(nums)

sp = sum(nums) / n
nums.sort()
mid = nums[n//2]

# 최빈값
for i in range(1, len(nums)):
    # dict[i] = nums.count(i)
    if nums[i-1] == nums[i]:
        dict[nums[i]] += 1
print(dict)
m_key = [k for k, v in dict.items() if max(dict.values()) == v]           # 최대 value 값에 대한 key 값 반환

if len(m_key) == 1:          # 최빈값
    mode = m_key[0]
else:                       # 최빈값이 여러 개일 때, 2번째로 작은 값 출력
    m_key.sort()
    mode = m_key[1]

r = abs(max(nums) - min(nums))

print(round(sp), mid, mode, r, sep='\n')