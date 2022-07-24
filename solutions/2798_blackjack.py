N, M = map(int, input().split())
card = list(map(int, input().split()))

best = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            test =card[i] + card[j] + card[k]
            if best < test <= M:
                best = test

print(best)
