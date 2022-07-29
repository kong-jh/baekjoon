N = int(input())
data = list(map(int, input().split()))

rightmost = [-1]*N
stack = []

for i in range(N):
    while stack and data[stack[-1]] < data[i]:
        rightmost[stack[-1]] = data[i]
        del stack[-1]
    stack.append(i)

print(*rightmost)
