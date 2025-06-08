import sys
from collections import deque

def preorder(tree):
    stk1 =[]

    stk1.append([list(tree.keys())[0], False])
    str1 =''
    while stk1:
        temp = stk1.pop()
        if temp[1] == True:
            str1+=temp[0]
            continue
        #str1 += temp
        if tree.get(temp[0])[1] != ".":
            stk1.append([tree.get(temp[0])[1], False])
        if tree.get(temp[0])[0] != ".":
            stk1.append([tree.get(temp[0])[0], False])
        stk1.append([temp[0],True])
            
        #print(tree.get(temp)[0])
        #print(tree.get(temp)[1])
    
    print(str1)
    
    return

def inorder(tree):
    stk1 =[]

    stk1.append([list(tree.keys())[0], False])
    str1 =''
    while stk1:
        temp = stk1.pop()
        if temp[1] == True:
            str1+=temp[0]
            continue
        #str1 += temp
        if tree.get(temp[0])[1] != ".":
            stk1.append([tree.get(temp[0])[1], False])
        stk1.append([temp[0],True])
        if tree.get(temp[0])[0] != ".":
            stk1.append([tree.get(temp[0])[0], False])
            
        #print(tree.get(temp)[0])
        #print(tree.get(temp)[1])
    
    print(str1)
    
    return

def postorder(tree):
    stk1 =[]

    stk1.append([list(tree.keys())[0], False])
    str1 =''
    while stk1:
        temp = stk1.pop()
        if temp[1] == True:
            str1+=temp[0]
            continue
        #str1 += temp
        stk1.append([temp[0],True])
        if tree.get(temp[0])[1] != ".":
            stk1.append([tree.get(temp[0])[1], False])
        if tree.get(temp[0])[0] != ".":
            stk1.append([tree.get(temp[0])[0], False])
    
    print(str1)
    
    return


tree = {}
stk = []
n = int(input())

#print(tree)


#insert
for _ in range(n):
    indata = list(sys.stdin.readline().strip().split(" "))
    
    stk.append(indata[0])
    tree[stk.pop()] =[indata[1],indata[2]]

print(tree)
preorder(tree)
inorder(tree)
postorder(tree)


    
    
    
    

            
        
    

