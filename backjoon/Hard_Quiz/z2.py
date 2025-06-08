#z2 한번더

import sys
sys.stdin = open("input.txt","r")
N,r,c  = map(int ,sys.stdin.readline().split(' '))
def z(N,r,c):
    ans = 0
    if N==0:
        ans +=1
        return ans
    N-=1      
    if r < N and r < N:
        ans = z(N,r,c)
    if r >= N and c < N:
        ans = 2**N+z(N,r,c)
    if r < N and c >= N:
        ans = (2**N*3)-1+z(N,r,c)
    if r >= N and c >= N:
        ans = 2**N+z(N,r,c)
        
    return ans

print(z(N,r,c))