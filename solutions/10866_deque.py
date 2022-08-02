import sys
input = sys.stdin.readline

maxQue = 10000
data = [0]*maxQue
f = 0
b = 0

N = int(input())

for _ in range(N):
    cmd = input().split()
    #print(f, b, data)

    if cmd[0] == 'push_front':
        f = (f-1)%maxQue
        data[f] = int(cmd[1])


    elif cmd[0] == 'push_back':
        data[b] = int(cmd[1])
        b = (b+1)%maxQue

    elif cmd[0] == 'pop_front':
        if f == b:
            print(-1)
        else:
            print(data[f])
            f = (f+1)%maxQue

    elif cmd[0] == 'pop_back':
        if f == b:
            print(-1)
        else:
            b = (b-1)%maxQue
            print(data[b])

    elif cmd[0] == 'size':
        if f <= b:
            print(b-f)
        else:
            print(maxQue-f + b)

    elif cmd[0] == 'empty':
        if f == b:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if f == b:
            print(-1)
        else:
            print(data[f])

    elif cmd[0] == 'back':
        if f == b:
            print(-1)
        else:
            print(data[(b-1)%maxQue])
