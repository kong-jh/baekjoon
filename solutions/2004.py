n, m = map(int, input().split())

def two(n):
    cnt = 0
    d = 2
    while d <= n:    
        cnt += (n//d)
        d *= 2
        
    return cnt

def five(n):
    cnt = 0
    d = 5
    while d <= n:
        cnt += (n//d)
        d *= 5
    return cnt


t = two(n) - (two(n-m) + two(m))
f = five(n) - (five(n-m) + five(m))

print(min(t, f))
