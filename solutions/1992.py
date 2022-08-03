def compression(n, arr):
    check = True
    val = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != val:
                check = False

    if check:
        print(val, end='')
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
        
        print('(', end='')
        compression(n//2, a)
        compression(n//2, b)
        compression(n//2, c)
        compression(n//2, d)
        print(')', end='')

N = int(input())
data = []

for _ in range(N):
    data.append(input())

print(data)
compression(N, data)
