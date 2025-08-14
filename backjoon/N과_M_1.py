import sys

def work():
    if len(s) == m:
        print(' '.join(map(str,s)))
    
    elif len(s) > m:
        return
    
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            s.append(i)
            work()
            s.pop()
            visited[i] = False

        
        
        

n,m = map(int,sys.stdin.readline().split())
visited=[False for _ in range(n+1)]
s= []
#dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

work()
        

