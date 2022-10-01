import sys
input = sys.stdin.readline

N = int(input())

e = []
for i in range(N):
    e.append(list(map(int, input().split())))
e.sort()

dp = [0]*N
for i in range(N):
    for j in range(i):
        
        if e[i][1] > e[j][1] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1

print(N-max(dp))
