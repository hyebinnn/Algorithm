T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    result = [""] * n
    totalScore = []
    for i in range(n):
        middle, final, assignment = map(int, input().split())
        total = middle * 0.35 + final * 0.45 + assignment * 0.2
        totalScore.append((i, total))
    
    totalScore = sorted(totalScore, key=lambda x: x[1], reverse=True)
    interval = n//10
    for gradeIndex, i in enumerate(range(0, n, interval)):
        for j in range(i, i+interval):
            result[totalScore[j][0]] = grade[gradeIndex]
        
    print(f"#{test_case} {result[k-1]}")
        