N, M = map(int, input().split())

state = ['']*N
target = ['B', 'W']
target2 = ['W', 'B']
loc = 0

for i in range(N):
    state[i] = input()
    
min_num = N*M
for i in range(N-7):
    for j in range(M-7):
        diff1 = 0
        diff2 = 0
        print("[",i, j,"]")
        for a in range(i, i+8):
            loc = (loc+1)%2
            print(state[a][j:j+8], target[loc], target2[loc])
            for b in range(j, j+8):
                if state[a][b] != target[loc]:
                    diff1 += 1
                if state[a][b] != target2[loc]:
                    diff2 += 1
                loc = (loc+1)%2
        if min(diff1, diff2) < min_num:
            min_num = min(diff1, diff2)

print(min_num)
