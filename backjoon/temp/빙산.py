import sys
from collections import deque
#sys.stdin = open('input.txt','r')

n,m = map(int,sys.stdin.readline().split())

#print(n,m)
direction= [(-1,0),(1,0),(0,-1),(0,1)]
place= []
year = 0
memo = {}
for _ in range(n):
    place.append(list(map(int,sys.stdin.readline().split())))
    

while True:
    
    year+=1
    for y in range(1,n-1):
        for x  in range(1,m-1):
            cnt=0
            for dy,dx in direction:
                if place[y+dy][x+dx] == 0:
                    cnt+=1
            place[y][x] -= cnt
            if place[y][x] < 0:
                place[y][x] = 0
            else:
                memo[(y,x)]= 0
    
    ##dfs



       
               

                    
                    
    
    #print(place)       
            

print(place)