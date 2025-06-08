import sys

def my_power(a,b, c):
    if b == 0:
        return 1
    if b % 2 == 0:
        mp = my_power(a,b//2, c) 
        return  (mp * mp) % c
    if b % 2 == 1:
        mp = my_power(a,b//2, c)
        return  (mp * mp * a )% c 



a,b,c = map(int, sys.stdin.readline().split(' '))
result = my_power(a,b,c )
print(result)