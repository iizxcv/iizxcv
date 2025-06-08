import sys

n, acount = map(int,input().split())

coins=[]
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
    
#coins.sort(reverse=True)
#print(coins)
result = 0
while coins:
    coin = coins.pop()
    result += acount//coin
    acount %= coin

print(result)
    