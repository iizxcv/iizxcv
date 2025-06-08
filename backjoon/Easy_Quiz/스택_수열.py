import sys

n = int(input())


data = []
for _ in range(n):
    
    data.append(int(sys.stdin.readline()))
    
stk = [0]
stk2 = []
result = []
for _ in range(n):
    if stk or stk[-1] < _ :
        for i in range(stk[-1]+1,data[_]+1): 
            if i not in stk2: 
                stk.append(i)
                result.append("+")
                #print("+")
    stk2.append(stk.pop())
    result.append("-")
    #print("-")


#print(stk)
#print(stk2)

if n == len(stk2):
    for _ in result:
        print(_)
else:
    print("NO")

        
            
            
    
       
       