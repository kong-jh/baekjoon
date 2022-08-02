N, K = map(int, input().split())
data = list(map(int, input().split()))
temp = []

temp.append(sum(data[:K]))

i=0
while i+K < N:
    temp.append(temp[i]-data[i] + data[i+K])
    i+=1
    
print(max(temp))
