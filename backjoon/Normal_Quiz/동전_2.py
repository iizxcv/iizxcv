import sys
from collections import deque
#sys.stdin = open('input.txt','r')


n,k = map(int, sys.stdin.readline().split())
coins = [0] * n

for _ in range(n):
    coins[_] = int(sys.stdin.readline())

dp={} 
coins.sort(reverse=True)
#print(coins)
cnt = 1
coins_q = deque()
ans = -1
for coin in coins:
    coins_q.append((coin,cnt))
    dp[coin] = 1
    
while True:   
    if coins_q:
        tot,cur_cnt = coins_q.popleft()

        
        if k == tot:
            ans = cur_cnt
            break

        for coin in coins:
            next_tot = tot + coin
            if next_tot <= k:
                if next_tot not in dp or dp[next_tot] > cur_cnt + 1:
                    dp[next_tot] = cur_cnt + 1
                    coins_q.append((next_tot, cur_cnt + 1))
    else:
        break
print(ans)    