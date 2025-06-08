import sys

def numset(tot,data,n):
    global cnt
    #print(data)
    global memo
    

    for i in range(n,len(data)):
        
        memo.append(data[i])
        if n <= len(data):   
            numset(tot,data,i+1)
        if sum(memo) == tot:
            cnt+=1
        memo.pop()

    
    


n, tot = map(int, sys.stdin.readline().split())

data=(sys.stdin.readline().strip('\n').split(' '))

data=list(map(int,data))


memo=[]
cnt = 0
numset(tot,data,0)
print(cnt)

