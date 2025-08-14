import sys
import math


n = int(sys.stdin.readline())
for _ in range(n):
    cnt = 0
    min_paper = math.inf
    min_interview = math.inf
    lst1= []
    nn = int(sys.stdin.readline())
    
    for _ in range(nn):
        lst1.append(tuple(map(int,sys.stdin.readline().split())))
    lst1.sort()
    
    for paper,interview in lst1:
        if paper < min_paper or interview < min_interview:
            cnt+=1
            min_paper = min(min_paper, paper)
            min_interview= min(min_interview, interview)

            
    print(cnt)
