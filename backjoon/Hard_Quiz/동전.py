import sys

loop = int(sys.stdin.readline())

for _ in range(loop):
    c = int(sys.stdin.readline())
    coins= list(map(int,sys.stdin.readline().split()))
    tot = int(sys.stdin.readline())

    dp=[[0 for _ in range(tot+1)]for _ in range(len(coins))]

    for i in range(len(coins)):
        for j in range(tot+1):
            #print(coins[i])
            if j == 0:
                dp[i][j] = 0
            if i == 0 and j%coins[i] == 0:
                dp[i][j] =  1
            else:
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
    print(dp[-1][-1])
                


            
            




    
    
    