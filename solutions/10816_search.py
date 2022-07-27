import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
my_card = {}

for x in cards:
    if x not in my_card:
        my_card[x] = 0
    my_card[x] += 1
    
M = int(input())
card = list(map(int, input().split()))

for x in card:
    if x in my_card:
        print(my_card[x], end=' ')
    else:
        print(0, end=' ')
