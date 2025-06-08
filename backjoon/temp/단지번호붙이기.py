import sys
from collections import deque
#sys.stdin = open('input.txt','r')
n =int(input())


def home_dfs(arr,hos):
    cnt=1
    while hos:
        cur_y,cur_x = hos.popleft()
        arr[cur_y][cur_x] = 0
        for dy,dx in direction:
            if 0 <= cur_y+dy < n and 0 <= cur_x+dx < n:
                if arr[cur_y+dy][cur_x+dx] == 1:
                    arr[cur_y+dy][cur_x+dx] = 0
                    hos.append((cur_y+dy,cur_x+dx))
                    cnt+=1
    #print(cnt)
    homes.append(cnt)


arr= []
homes = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]
q = deque()
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip())))

for y in range(n):
    for x in range(n):
        if arr[y][x] == 1:
            q.append((y,x))
            home_dfs(arr,q)

homes.sort()
print(len(homes))
for h in homes:
    print(h)

