import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = list(map(int, input().split()))


for i in range(1, N):
    data[i] += data[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(data[j-1])
    else:
        print(data[j-1] - data[i-2])
