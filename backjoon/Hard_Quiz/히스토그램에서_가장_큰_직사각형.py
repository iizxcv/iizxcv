import sys

def check_box(start,end):
    
    if start == end:
        return histo[start]


    mid = (start+end) //2
    left_area = check_box(start,mid)
    right_area = check_box(mid+1,end)
    
    low = mid
    high = mid +1
    height = min(histo[low],histo[high])
    boxsize = height *2
    
    while start < low or high < end:
        if high < end and (low == start or histo[low-1]) < histo[high+1]:
            high +=1
            height = min(height,histo[high])
        else:
            low -= 1
            height = min(height, histo[low])  
        boxsize= max(boxsize, height * (high-low +1))
    return max(left_area,right_area,boxsize)



result = []

while True:
    
    histo = list(map(int, sys.stdin.readline().split(' ')))
    if histo[0] == 0:
        break
    else:
        
        histo= histo[1:]

        #print(max_val)
        #print(histo)
        result.append(check_box(0,len(histo)-1))
        
for _ in result:
    print(_)