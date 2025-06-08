import sys

num = int(sys.stdin.readline())
cnt =0
sticks=[]
for _ in range(num):
     temp = int(sys.stdin.readline())
     sticks.append(temp)
max1=0
for _ in range(len(sticks)-1,-1,-1):
    temp = sticks.pop()
    if max1 < temp:
        max1 = temp
        cnt+=1

print(cnt)
#print(temp)

         
     
    