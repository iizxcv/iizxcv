import sys
import math
import time
start = time.time()
math.factorial(100000)

#n = int(input())

arr = [10,1,3,2,4,3,5,4,6,5,7]

dp = [1]*len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
end = time.time()
print(f"{end - start:.5f} sec")