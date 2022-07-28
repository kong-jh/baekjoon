T = int(input())

for _ in range(T):
    x1, y1 ,r1, x2, y2, r2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1) # 원 교차 -> 무한대
        else:
            print(0) # 원 안에 다른 원 포함
    else:
        diff = ((x2-x1)**2 + (y2-y1)**2)**0.5

        # 두 점
        if abs(r1-r2) < diff < r1+r2:
            print(2)
        # 한 점
        elif diff == r1+r2 or max(r1, r2) == diff + min(r1, r2):
            print(1)
        # 만나지 않음
        else:
            print(0)
