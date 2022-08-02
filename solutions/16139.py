import sys
input = sys.stdin.readline

s = input().strip()
q = int(input())

cnt = [[0]*26]

for i in range(len(s)):
    cnt.append(cnt[-1][:])
    cnt[i+1][ord(s[i])-ord('a')] += 1

# print(cnt)

for _ in range(q):
    a, l, r = input().split()
    l, r= int(l), int(r)
    print(cnt[r+1][ord(a)-ord('a')] - cnt[l][ord(a)-ord('a')])
