def star(n):
    if n == 3:
        s[0][:3] = s[2][:3] = [1]*3
        s[1][:3] = [1, 0, 1]
        return

    else:
        a = n//3
        star(a)

        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    for k in range(a):
                        s[i*a+k][j*a:j*a+a] = s[k][:a]

N = int(input())
s = [[0]*N for i in range(N)]
star(N)

for i in range(N):
    for j in range(N):
        if s[i][j]:
            print("*", end='')
        else:
            print(" ", end='')
    print()
