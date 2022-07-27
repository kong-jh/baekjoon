import sys
input = sys.stdin.readline

N = int(input())
my_card = set(map(int, input().split()))

M = int(input())
card = list(map(int, input().split()))

for x in card:
    if x in my_card:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
