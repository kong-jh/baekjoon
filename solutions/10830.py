N, B = map(int, input().split())
m = 1000

def mult(a, b):
    result = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k]*b[k][j]
            result[i][j] %= 1000
    return result

def power(a, n):
    if n==1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    else:
        if n%2 == 0:
            x = power(a, n//2)
            result = mult(x, x)
        else:
            x = power(a, n//2)
            y = mult(x, a)
            result = mult(x, y)

        return result

data = [list(map(int, input().split())) for i in range(N)]

for i in power(data, B):
    for j in i:
        print(j, end=' ')
    print()
