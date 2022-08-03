global blue
global white

blue = 0
white = 0

def partition(n, arr):
    global blue
    global white

    print(n, arr)
    if n == 1:
        if arr[0][0]:
            blue += 1
        else:
            white += 1
    else:
        check = True
        color = arr[0][0]
        for i in range(n):
            for j in range(n):
                if arr[i][j] != color:
                    check = False

        if check:
            if color:
                blue += 1
            else:
                white += 1
        else:
            a = []
            b = []
            c = []
            d = []
            for i in range(n//2):
                a.append(arr[i][:n//2])
                b.append(arr[i][n//2:])
            for i in range(n//2, n):
                c.append(arr[i][:n//2])
                d.append(arr[i][n//2:])

            partition(n//2, a)
            partition(n//2, b)
            partition(n//2, c)
            partition(n//2, d)

N = int(input())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

print(partition(N, paper))
