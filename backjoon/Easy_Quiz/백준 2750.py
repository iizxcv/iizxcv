#백준 2750
import sys

n = int(input())

a=[0 for _ in range(n)]
#print(a)
for i in range(0, len(a)):
    a[i] = sys.stdin.readline()

#a.sort(reverse=False)
a.sort()

for i in a:
    print(i)