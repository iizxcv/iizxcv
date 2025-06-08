import sys

no, routers = map(int,input().split(' '))

home = []

for _ in range(no):
    home.append(int(sys.stdin.readline().strip()))

home.sort()
start=1
end = home[-1] - home[0]
result = 0

cnt = 0
while start <= end:
    mid = (start + end) //2
    cnt =1
    pivot = 0
    
    for i in range(1,len(home)):
        if home[i] - home[pivot] >= mid:
            cnt+=1
            pivot = i
    #print(mid)
    if routers <= cnt:
        result = mid
        start = mid+1
        
    else: end = mid - 1
            
print(result)
