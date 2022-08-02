import collections

N, M = map(int, input().split())
sel = list(map(int, input().split()))

q = collections.deque([i for i in range(1, N+1)])

cnt = 0
for x in sel:
    if q.index(x) <= len(q)//2:
        while q[0] != x:
            cnt += 1
            q.append(q.popleft())
        q.popleft()
    else:
        while q[0] != x:
            cnt += 1
            q.appendleft(q.pop())
        q.popleft()

print(cnt)
