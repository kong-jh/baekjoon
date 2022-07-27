data = list(map(int, input().split()))

while 0 not in data:
    a = max(data)
    data.remove(a)

    if (a**2 == data[0]**2 + data[1]**2):
        print("right")
    else:
        print("wrong")
        
    data = list(map(int, input().split()))
