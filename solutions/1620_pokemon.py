import sys
input = sys.stdin.readline

N, M = map(int, input().split())

book1 = {}
book2 = {}

for i in range(1, N+1):
    x = input().strip()
    book1[x] = i
    book2[i] = x

for i in range(M):
    q = input().strip()
    if ord('1') <= ord(q[0]) <= ord('9'):
        print(book2[int(q)])
    else:
        print(book1[q])
