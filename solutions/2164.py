N = int(input())

cnt = 1
r = 0

while True:
    if N == 1:
        print(1)
        break
    if N // 2**cnt == 1 and N % 2**cnt == 0:
        print(2**cnt)
        break
    elif N // 2**cnt > 1:
        cnt += 1
    else:
        print((N % 2**cnt)*2)
        break



