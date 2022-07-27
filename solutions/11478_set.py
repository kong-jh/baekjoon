S = input().rstrip()
sub = set()

for i in range(1, len(S)):
    itr = 0
    while itr+i <= len(S):
        sub.add(S[itr:itr+i])
        itr += 1

print(len(sub)+1)
