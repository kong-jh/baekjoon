import sys
input = sys.stdin.readline

N, M = map(int, input().split())
no_listen = set()
no_see = set()

for i in range(N):
    no_listen.add(input().rstrip())

for i in range(M):
    no_see.add(input().rstrip())

no_both = sorted(list(no_listen.intersection(no_see)))
print(len(no_both))

for person in no_both:
    print(person)
