n = int(input())

data = []
idx = 0
check = True

seq = []
for i in range(n):
    x = int(input())

    while idx < x:
        idx+=1
        data.append(idx)
        
        seq.append('+')
        
    if data[-1] != x:
        check = False
        break
    
    seq.append('-')
    del data[-1]

if check:
    for i in seq:
        print(i)
else:
    print("NO")
