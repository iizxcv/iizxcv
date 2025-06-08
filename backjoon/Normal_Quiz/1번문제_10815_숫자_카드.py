import sys

def compare(s,e,n):
    left = s
    right = e
    #mid = left + right //2
    
    
    while left<=right:
        mid = (left + right) //2
        
        if input_data[mid] == n:
            return 1
        
        elif input_data[mid] < n:
            left = mid+1
        elif input_data[mid] > n:
            right = mid-1
    
    return 0
            
    



in_n = int(sys.stdin.readline())

input_data = [None]*in_n
input_data = list(map(int,sys.stdin.readline().split(" ")))
input_data.sort()
#print( input_data)

compare_n = int(sys.stdin.readline())
compare_data = list(map(int,sys.stdin.readline().split(" ")))

#print(compare(0,len(input_data)-1,2))

for _ in compare_data:
    print(compare(0,len(input_data)-1,_), end=" ")



