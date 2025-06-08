from itertools import permutations
import sys
sys.stdin = open("input.txt","r")

#(1) 순열만들기
input = sys.stdin.readline
n = int(input())

arr = (list(map(int, input().split())))

p = list(permutations(arr,n))

result =0
for i in p:
    #print(i)
    s= 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    
    result=max(result, s)   
    
print(result) 
