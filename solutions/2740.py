import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for i in range(M)]

def mult(a, b):
    result = [[0 for col in range(K)] for row in range(N)]
    for i in range(N):
        for j in range(K):
            for k in range(M):
                result[i][j] += A[i][k] * B[k][j]

    return result

for i in mult(A, B):
    for j in i:
        print(j, end= ' ')
    print()
