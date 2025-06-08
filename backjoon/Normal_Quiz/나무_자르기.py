import sys

def tree_cut(trees,n):
    tot = 0
    for tree in trees:
        if tree-n > 0:
            tot += tree-n
    
    return tot
    

def search_height(start,end,trees):
    global value
    mid = (start+end)//2
    tot = tree_cut(trees,mid)
     
    
    #print(mid)
    if tot == value:
        print(f'{mid}')
        return

    if value > tot:
        search_height(start,mid-1,trees)
    elif value < tot:
        search_height(mid+1,end,trees)
    
    return
    

num,value = map(int,sys.stdin.readline().split())

trees= list(map(int,sys.stdin.readline().split()))

start = 0
end = max(trees)
search_height(start,end,trees)
#print(trees)