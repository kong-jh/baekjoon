import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

print(data)

for i in range(N):
    for j in range(1, N):
        data[i][j] += data[i][j-1]
    print(data[i])

for i in range(1, N):
    for j in range(N):
        data[i][j] += data[i-1][j]
    print(data[i])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(data[x2-1][y2-1])
    elif x1 == 1:
        print(data[x2-1][y2-1] - data[x2-1][y1-2])
    elif y1 == 1:
        print(data[x2-1][y2-1] - data[x1-2][y2-1])
    else:
        print(data[x2-1][y2-1] - data[x2-1][y1-2] - data[x1-2][y2-1] + data[x1-2][y1-2])
