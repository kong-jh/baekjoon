W, H, X, Y, P = map(int, input().split())
cnt = 0

for i in range(P):
    x, y = map(int, input().split())
    if Y <= y <= Y+H:
        if X <= x <= X+W:
            cnt += 1
        elif x <= X:
            diff = ((X-x)**2 + ((Y+H//2)-y)**2)**0.5
            if diff <= H//2:
                cnt += 1
        elif x <= (X+W+H//2):
            diff = ((X+W-x)**2 + ((Y+H//2)-y)**2)**0.5
            if diff <= H//2:
                cnt += 1
print(cnt)
