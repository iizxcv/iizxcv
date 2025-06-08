import sys

def bfs_search(left,right,target):
    if left > right:
        return 0;

    mid = (left+right)//2
    
    if arr1[mid] == target:
        return 1

    
    elif arr1[mid] > target:
        return bfs_search(left,mid-1,target)
    
    elif arr1[mid]  < target:
        return bfs_search(mid+1,right,target)

num1 = int(sys.stdin.readline())

arr1 = list(map(int,sys.stdin.readline().split(' ')))

arr1.sort()
#print(arr1)

num2 = int(sys.stdin.readline())

arr2 = list(map(int,sys.stdin.readline().split(' ')))

a_len = len(arr1)

for i in arr2:
    print(bfs_search(0,a_len-1,i))    

