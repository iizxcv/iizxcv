import sys

def parentheses_check(n):
    stk = []
    for _ in n:
        if _ == "(":
            stk.append(1)
        elif _ == ")":
            if len(stk) == 0:
                return print("NO") 
            stk.pop()
        
    if stk :
            return print("NO")
        
    else:
        return print("YES")
                
        
            


n = int(input())

for _ in range(n):
    i =list(sys.stdin.readline())
    parentheses_check(i)


