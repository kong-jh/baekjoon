import sys
input = sys.stdin.readline

n = int(input())
step = []
step.append([0, 0, 0])

for i in range(n):
    step.append([int(input()), 0, 0])

step[1][1] = step[1][2] = step[1][0]

for i in range(2, n+1):
    # 1 step
    step[i][1] = step[i-1][2] + step[i][0]

    # 2 step
    step[i][2] = max(step[i-2]) + step[i][0]

print(max(step[n]))
