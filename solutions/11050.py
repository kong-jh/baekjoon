def binomial(n, k):
    B = [[0 for col in range(k+1)] for row in range(n+1)]

    for i in range(n+1):
        for j in range(0, min(k, i)+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    return B[n][k]

n, k = map(int, input().split())
print(binomial(n, k))
