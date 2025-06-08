import sys

n = int(input())
fibo =[0 for _ in range(n+1)]
i = 2
if n < 2:
    print(n)
else:
    fibo[0] = 0
    fibo[1] = 1
    while i <= n:
         fibo[i]=fibo[i-2]+fibo[i-1]
         i+=1

    print(fibo[n])
