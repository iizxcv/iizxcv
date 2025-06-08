import sys

#sys.stdin = open("input.txt","r")

def make(n):
     
    left_lst = list(str(n))
    
    left_lst = list(map(int, left_lst))
    #print(left_lst)

    if len(left_lst) == 1:
        left_lst.insert(0,0)
    
    
    temp=left_lst
    
    return temp

def cicle(ref,lst_prev,cnt):


    
  
    n = lst_prev[0] + lst_prev[1]

    if cnt != 0:
        compare1 =(lst_prev[0]*10) +(lst_prev[1])
        if compare1 == ref:
            return cnt
    cnt +=1
    
    #print(compare1)

    lst_next =make(n)
    cnt = cicle(ref,[lst_prev[1],lst_next[1]],cnt)
    return cnt

n = int(sys.stdin.readline())

print(cicle(n,make(n),0))

