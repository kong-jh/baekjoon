import sys
input = sys.stdin.readline

data = []
f = 0

N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        data.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(data)-f == 0:
            print(-1)
        else:
            print(data[f])
            f += 1
    elif cmd[0] == 'size':
        print(len(data)-f)
    elif cmd[0] == 'empty':
        if len(data)-f == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(data)-f == 0:
            print(-1)
        else:
            print(data[f])
    elif cmd[0] == 'back':
        if len(data)-f == 0:
            print(-1)
        else:
            print(data[-1])
