n = int(input())

base = [[1, 1], [1, 0]]
m = 1000000007

def mult(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k]*b[k][j]
            result[i][j] %= m
    return result

def fib(n):
    if n == 1:
        return base
    else:
        if n % 2 == 0:
            x = fib(n//2)
            return mult(x, x)
        else:
            x = fib(n//2)
            y = mult(x, base)
            return mult(x, y)

if n == 0:
    print(0)
else:
    print(fib(n)[0][1])
