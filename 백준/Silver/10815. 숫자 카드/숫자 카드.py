import sys

n = int(sys.stdin.readline())
a = set(map(int,sys.stdin.readline().split()))
n2 = int(sys.stdin.readline())
a2 = list(map(int,sys.stdin.readline().split()))

result = []

for x in a2:
    if x in a:
        print(1, end=" ")
    else:
        print(0, end=" ")