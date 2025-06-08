import sys
n, k = map(int, input().split())

zxcv = [[0,0]] 
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    zxcv.append(list(map(int, input().split()))) 

zxcv.sort()

for i in range(1,n+1):
    w = zxcv[i][0]
    v = zxcv[i][1] 
    for j in range(1,k+1):
        if j < w:
            d[i][j] = d[i-1][j]
        else: 
            d[i][j] = max(d[i-1][j],d[i-1][j-w]+v)

print(d[-1][-1])