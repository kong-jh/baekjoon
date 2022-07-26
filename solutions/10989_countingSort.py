import sys
input = sys.stdin.readline

N = int(input())
counting = [0]*10001

for i in range(N):
    x = int(input())
    counting[x] += 1

for i in range(1, 10001):
    for j in range(counting[i]):
        print(i)
