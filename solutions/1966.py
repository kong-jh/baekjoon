import collections
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    doc = collections.deque()
    data = list(map(int, input().split()))

    for i in range(N):
        doc.append([i, data[i]])

    cnt = 0
    printer = -1
    while printer != K:
        best = max(doc, key=lambda x:x[1])

        if doc[0] == best:
            printer = doc[0][0]
            doc.popleft()
            cnt += 1

        else:
            while doc[0] != best:
                doc.append(doc.popleft())
    print(cnt)
