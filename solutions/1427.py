import sys
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num.sort()

print(round(sum(num)/N))   
print(num[N//2])

frequency = {}
for i in num:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

maxf = list(frequency.values())

if maxf.count(max(maxf)) == 1:
    for key, value in frequency.items():
        if max(maxf) == value:
            print(key)
else:
    most = []
    for key, value in frequency.items():
        if max(maxf) == value:
            most.append(key)
    most.sort()
    print(most[1])

print(max(num)-min(num))
