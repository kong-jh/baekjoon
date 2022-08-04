a, b, c = map(int, input().split())

def remain(n):
    if n == 1:
        return a%c
    else:
        if n % 2 == 0:
            return remain(n//2)**2 % c
        else:
            return remain(n//2)**2*a % c

print(remain(b))
