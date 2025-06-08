import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

stack = []
# 인덱스와 탑의 높이
stack.append([1, towers[0]])
# 맨 왼쪽 탑은 수신되지 않음
result = [0]

for i  in range(1,n): #n번 반복
    while stack: #스텍값이 존재하면 반복
        if towers[i] < stack[-1][1]:
            result.append(stack[-1][0])
            stack.append([i+1,towers[i]])
            break
        else: 
            stack.pop()
                        
        
    if not stack:
        result.append(0)
        stack.append([i+1,towers[i]])
    
for _ in result:
    print(_,end=' ')  
            
