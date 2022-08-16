import sys
input = sys.stdin.readline

def fib(n):
    f = [1, 1, 1]
    for i in range(3, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

n = int(input())

print(fib(n), n-2)
