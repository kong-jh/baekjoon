import sys
input = sys.stdin.readline

N = int(input())

words = []

for i in range(N):
    words.append(input().strip())


words.sort(key = lambda x : (len(x),x))

for i in range(N):
    if i != 0 and words[i-1] == words[i]:
        continue
    else:
        print(words[i])
