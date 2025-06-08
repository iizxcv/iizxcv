import sys
from collections import deque
#sys.stdin.read()
sys.stdin = open('input.txt', 'r')

map_y, map_x = map(int,sys.stdin.readline().split())

#print(map_x,map_y)

map1= []
for _ in range(map_y):
    map1.append(list(sys.stdin.readline().rstrip()))

#print(map1)

sonic = (0,0)
dst = (0,0)
stone = (0,0)
fluid = deque()
#초기 위치 지정
for y in range(map_y):
    for x in range(map_x):
        if map1[y][x] == "D":
            dst= (y,x)
        elif map1[y][x]== "*":
            fluid.append((y,x))
        elif map1[y][x]== "S":
            sonic =(y,x)

            
direction = [(-1,0),(1,0),(0,-1),(0,1)]

sonic_bfs = deque()
sonic_bfs.append((sonic[0],sonic[1],0))
fluid_bfs = deque()
for fy, fx in fluid:
    fluid_bfs.append((fy, fx))
time = 0
while True:
    
    
    
    if map1[dst[0]][dst[1]] != 'D':
        break
    
    for _ in range(len(fluid_bfs)):
        fx,fy = fluid_bfs.popleft()
        for dy,dx in direction:
            if  0 <= fy+dy < map_x and 0 <= fx+dx < map_y:
                if map1[(fx+dx)][(fy+dy)] == '.':
                    map1[(fx+dx)][(fy+dy)] = '*'
                    fluid_bfs.append((fx+dx,fy+dy))
    
    if not sonic_bfs:
        print("KAKTUS")
        break
    
    for _ in range(len(sonic_bfs)):
        cx,cy,cost = sonic_bfs.popleft()
        for dy,dx in direction:
            if  0 <= cy+dy < map_x and 0 <= cx+dx < map_y:
                if map1[(cx+dx)][(cy+dy)] == ('.'):
                    map1[(cx+dx)][(cy+dy)] = cost+1
                    sonic_bfs.append((cx+dx,cy+dy,cost+1))
                elif map1[(cx+dx)][(cy+dy)] == ('D'):
                    print(cost+1)
                    map1[(cx+dx)][(cy+dy)] = cost+1

                
            
            
            