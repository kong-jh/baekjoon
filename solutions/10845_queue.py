import sys
input = sys.stdin.readline

data = []

N = int(input())

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        data.append(int(cmd[1]))

    elif cmd[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
            del data[0]

    elif cmd[0] == 'size':
        print(len(data))

    elif cmd[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])

    elif cmd[0] == 'back':
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
        
