"""
최대한 싸게 사고 비싸게 판매해야함
"""

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    selling = list(map(int, input().split()))
    
    res = 0

    def calculateBenefit(start):
        global res
        for i in range(maxIdx-1, start-1, -1):
            res += maxPrice - selling[i]
        
        
    temp = 0
    s = 0
    for _ in range(n):
        maxPrice = max(selling[s:])
        maxIdx = s + selling[s:].index(maxPrice)
        calculateBenefit(s)
        if maxIdx >= n-1:
            break
        s = maxIdx+1
    
    print(f"#{test_case} {res}")
    