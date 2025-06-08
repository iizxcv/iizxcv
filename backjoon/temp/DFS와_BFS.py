import sys
from collections import deque

sys.stdin = open('input.txt','r')

def bfs(check_v, edges):
    
    copy_vertexs = vertexs
    copy_edges = edges
    

    for _ in range(len(copy_edges)):
        a,b = copy_edges.popleft()
        check[a] 
        
    
    
    
    return  


n,m,v = map(int, sys.stdin.readline().split())

vertexs=[False for _ in range(n+1)]
edges = deque()

for e in range(m):
    a,b=map(int, sys.stdin.readline().split())
    edges.append((a,b))

edges.sort()





