cnt = {-1:0, 0:0, 1:0}

def cut(n, x, y):
    check = True
    val = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != val:
                check = False
                break

    if check:
        cnt[val] += 1
    else:
        n //= 3
        for i in range(3):
            for j in range(3):
                cut(n, x+i*n, y+j*n)

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

cut(N, 0, 0)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
