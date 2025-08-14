import sys
sys.setrecursionlimit(1000000)


n = int(sys.stdin.readline())

wines =[]
memo= [0 for _ in range(n)]

for _ in range(n):
    wines.append(int(sys.stdin.readline()))

if n >= 1: 
    memo[0] = wines[0]
if n >= 2:    
    memo[1] = memo[0]+wines[1]
if n >= 3: 
    memo[2] = max(wines[0]+wines[1], wines[0]+wines[2], wines[1]+wines[2])


def find(start):
    if n > 3:
        for i in range(3,n):
            memo[i] = max(
            memo[i-1],  # 이번 포도주 안 마심
            memo[i-2] + wines[i],  # 이번 포도주 마심, 직전은 안 마심
            memo[i-3] + wines[i-1] + wines[i]  # 이번+직전 마심, i-3까지의 최적값
        )
    else:return

        

find(0)
#print(memo)
print(max(memo))
