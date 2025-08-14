import sys

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        
        return
        
    for i in range(start,n+1):
        if visited[i] == False:
            visited[i]=True
            s.append(i)
            dfs(i+1)
            s.pop()
            visited[i] = False
    

n,m = map(int,sys.stdin.readline().split())
s=[]
visited =[False for _ in range(n+1)]

dfs(1)
