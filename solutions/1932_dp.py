import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))


for i in range(1, n): #층별
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][0]
        elif j == len(triangle[i]) -1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1:j+1])

print(max(triangle[n-1]))


