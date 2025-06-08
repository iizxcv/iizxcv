import sys

sys.stdin = open("input.txt","r")

x,y = map(int, sys.stdin.readline().split())
n =  int(sys.stdin.readline())

lst_x = [x]
lst_y = [y]

for _ in range(3):
    x1,y1 = map(int, sys.stdin.readline().split())
    if not(x1 in lst_x): lst_x.append(x1)
    if not(y1 in lst_y): lst_y.append(y1)

max_x =0
max_y =0
lst_x.sort()
lst_y.sort()

for i in range(len(lst_x)-1,0,-1):
    max_x = max(max_x,lst_x[i]-lst_x[i-1])
    
for i in range(len(lst_y)-1,-1,-1):
    max_y = max(max_y,lst_y[i]-lst_y[i-1])
print(lst_x,lst_y)
print(max_x,max_y)
    


