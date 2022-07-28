k = int(input())
line = []

for i in range(6):
    line.append(list(map(int, input().split())))
    
seq = [4, 2, 3, 1]
x = 0
while seq[x] != line[0][0]:
    x += 1

i = 0
while seq[x] == line[i][0]:
    x = (x+1)%4
    i = (i+1)%6

A = line[i][1] * line[(i-1)%6][1]
B = line[(i+2)%6][1] * line[(i+3)%6][1]
print((B-A)*k)
