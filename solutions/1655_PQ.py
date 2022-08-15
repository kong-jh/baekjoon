import heapq
import sys
input = sys.stdin.readline

N = int(input())

mid = int(input())
small = []
big = []
print(mid)

for _ in range(N-1):
    x = int(input())
    if x >= mid:
        heapq.heappush(big, x)
        if len(big) - len(small) > 1:
            heapq.heappush(small, -mid)
            mid = heapq.heappop(big)
    else:
        heapq.heappush(small, -x)
        if len(small) - len(big) > 0:
            heapq.heappush(big, mid)
            mid = -heapq.heappop(small)

    print(mid)         
