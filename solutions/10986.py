import math

N, M = map(int, input().split())
data = list(map(int, input().split()))

for i in range(1, N):
    data[i] += data[i-1]

remain = {}
for i in data:
    if i % M not in remain:
        remain[i%M] = []
    remain[i%M].append(i)

result = 0
if 0 in remain:
    result += len(remain[0])

for i in remain:
    result += math.comb(len(remain[i]), 2)

print(result)
