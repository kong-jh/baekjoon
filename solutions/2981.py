import math
import sys
input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    data.append(int(input()))

r =[]
for i in range(N-1):
    r.append(data[i] - data[i+1])

gcd = r[0]
for num in r:
    gcd = math.gcd(gcd, num)

M = set()
M.add(gcd)
for i in range(2, int(gcd**0.5)+1):
    if gcd % i == 0:
        M.add(i)
        M.add(gcd//i)

for i in sorted(M):
    print(i, end = ' ')
