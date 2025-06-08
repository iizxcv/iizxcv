import sys

def requid_mix(arr):
    
    result = 0
    
    start = 0
    end = len(arr)-1
    mid = abs((arr[start]+arr[end])//2 )
    mix_result = arr[start] + arr[end]
    a,b=0,0
    while start <= end:
        
        if abs(mix_result) >= abs(arr[start] + arr[end]):
            a = start
            b = end
        
            if abs(arr[start]) >= arr[end]:
                start+=1
            else:
                end-=1
        
        else: break
    
    print(arr[a],arr[b])
        #print(mix_result)
        


n = int(input())

arr=[]

arr = (list(map(int,sys.stdin.readline().split(' '))))
arr.sort()

requid_mix(arr)

#print(arr)