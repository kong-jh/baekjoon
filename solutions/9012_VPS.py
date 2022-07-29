T = int(input())

for _ in range(T):
    ps = input()
    cnt = 0

    if ps.count('(') != ps.count(')') or ps[0] == ')':
        print("NO")
        continue
    
    check = True
    for i in ps:
        if i == "(":
            cnt += 1
        else:
            cnt -=1
            if cnt < 0:
                check = False
                break
    if cnt != 0:
        check = False
        
    if check:
        print("YES")
    else:
        print("NO")
