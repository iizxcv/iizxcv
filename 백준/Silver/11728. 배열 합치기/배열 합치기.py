import sys

n,m = map(int,sys.stdin.readline().split())

l1 = []
l2 = []


l1 = list(map(int,sys.stdin.readline().split()))
l2 = list(map(int,sys.stdin.readline().split()))


l1.extend(l2)
l1.sort()

for x in l1:
    print(x ,end=" ")
