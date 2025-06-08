import sys
n = int(sys.stdin.readline())

if n < 2:
    print(n)
else:
    fibo= [0 for _ in range(n+1)]
    fibo[1] = 1
    fibo[2] = 2
    i = 3
    while i <= n:
        fibo[i] = (fibo[i-2]%15746 + fibo[i-1]%15746)%15746
        i+=1
    print(fibo[n])
    
