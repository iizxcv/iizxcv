import sys


n = int(sys.stdin.readline())
aa =[]
for _ in range(n):
    aa.append(tuple(map(int,sys.stdin.readline().split())))


paper = [[-1 for _ in range(100)] for _ in range(100)]

for a in aa:
    for x in range(a[0],a[0]+10):
        for y in range(a[1],a[1]+10):
            paper[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt +=1
            
print(cnt)
            