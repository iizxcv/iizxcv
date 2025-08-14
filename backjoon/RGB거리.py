import sys
import math
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
house = []
for _ in range(n):
    R,G,B = map(int,sys.stdin.readline().split())
    house.append([R,G,B])
    
memo = [[-1]*3 for _ in range(n)]
    
def find_min(i,color):
    if i == n:
        return
    if memo[i][color] != -1:
        return memo[i][color]
    elif i == 0:
        for _ in range(3):
            memo[i][_] = house[i][_]     
    else:
        for _ in range(3):
            memo[i][_] = min(memo[i-1][(_+1)%3],memo[i-1][(_+2)%3]) + house[i][_]
            
    find_min(i+1,0)
    find_min(i+1,1)
    find_min(i+1,2)

#print(result)
find_min(0,0)

print(min(memo[n-1][0],memo[n-1][1],memo[n-1][2]))