import itertools
import sys

def hobit_search(targets, total,num):

    for i in range(0,len(targets)):
        for j in range(i+1,len(targets)):
            if total-num == targets[i]+targets[j] :
                return targets[i],targets[j] 

    return [None]
                   
#sys.stdin = open('input.txt','r')

hobits =[]
for _ in range(9):

    hobits.append(int(sys.stdin.readline().strip("\n")))

total = sum(hobits)

#print(total)
del_hobit =hobit_search(hobits,total,100)

#print(del_hobit)

for _ in del_hobit:
    hobits.remove(_)
hobits.sort()

for _ in hobits:
    print(_)



