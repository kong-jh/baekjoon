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
        change = 0
        change2 = 0
        print("[",i, j,"]")
        for k in range(8):
            loc = (loc+1)%2
            print(state[i+k][j:j+8], target[loc], target2[loc])
            for l in range(8):
                if state[i+k][j+l] != target[loc]:
                    change += 1
                if state[i+k][j+l] != target2[loc]:
                    change2 += 1
                loc = (loc+1)%2
        if min(change, change2) < min_num:
            min_num = min(change, change2)

print(min_num)
