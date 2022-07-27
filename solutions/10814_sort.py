import sys
input = sys.stdin.readline

N = int(input())
user = []

for i in range(N):
    user.append(input().split())
    user[i][0] = int(user[i][0])

user.sort(key = lambda x : x[0])

for u in user:
    print(u[0], u[1])
