import sys
from collections import deque
sys.setrecursionlimit(10**6)
#sys.stdin = open('input.txt', 'r')


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    
    return p[x]

def union(s,d):
    root_s = find(s)
    root_d = find(d)
    
    if root_s != root_d:
        p[root_d] = root_s

n, m = map(int, sys.stdin.readline().split())

p = [a for a in range(n+1)]
edges = []
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))
    

edges.sort()
min_cost = 0
    
#print(edges)

for c,s,d in edges:
    if find(s) != find(d):
        union(s,d)
        min_cost += c

print(min_cost)
    
    
    