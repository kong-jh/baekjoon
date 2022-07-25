N = int(input())

people = [[0]*2 for i in range(N)]

for i in range(N):
    people[i] = list(map(int, input().split()))


rank = [1]*N
for i in range(N):
    for j in range(N):
        if j != i:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank[i] += 1

for r in rank:
    print(r, end=' ')
