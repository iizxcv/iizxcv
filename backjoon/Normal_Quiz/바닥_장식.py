import sys
#sys.stdin = open('input.txt','r')

def dfs_w(y,x):

    while 0 <= x < m and floor[y][x] == '-':
        visited[y][x] = True
        x+=1
    return 1

def dfs_h(y,x):
    
    while 0 <= y < n and floor[y][x] == '|':
        visited[y][x] = True
        y+=1
    return 1
       
n,m = map(int, sys.stdin.readline().split())
floor = []
for y in range(n):
    floor.append(list(sys.stdin.readline().strip()))
         
visited = [[False for _ in range(m)] for _ in range(n)]
cnt =0

for y in range(n):
    for x in range(m):
        if visited[y][x] == False:
            if floor[y][x] == '-':
                cnt +=dfs_w(y,x)
            else:
                cnt+= dfs_h(y,x)
                
            
print(cnt)
        