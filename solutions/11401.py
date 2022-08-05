import sys
input = sys.stdin.readline

n, k = map(int, input().split())
m = 1000000007

def fac(n):
    result = 1
    for i in range(2, n+1):
        result = result * i % m
    return result

def mod(a, b): #a^b -> a^b/2 * a^b/2
    if b == 0:
        return 1
    else:
        half = mod(a, b//2)
        if b % 2 == 0:
            return half ** 2 % m
        else:
            return (half)*(half*a) % m

x = fac(n)
y = (fac(n-k) * fac(k))


print((x%m)*(mod(y, m-2)%m)%m)

