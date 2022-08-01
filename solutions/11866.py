N, K = map(int, input().split())

circle = [i for i in range(1, N+1)]

idx = K-1
print('<', end='')
while len(circle) > 1:
    print(circle[idx], end=', ')
    del circle[idx]
    idx = (idx+K-1) % len(circle)

print(circle[0], '>', sep='')
