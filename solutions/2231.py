N = int(input())

result = 0

for i in range(N):
    num = i
    dsum = num
    while num != 0:
        dsum += (num%10)
        num //= 10

    if dsum == N:
        result = i
        break
        
print(result)
