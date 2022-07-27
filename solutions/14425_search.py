import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = set()

for i in range(N):
    words.add(input().strip())

cnt = 0
for i in range(M):
    word = input().strip()
    if word in words:
        cnt += 1

print(cnt)
