import sys

n,m = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip())))

memo= arr

#print(arr)


def big_rectangle(n,m):
    result = max(arr[0])

    for i in range(1,n):
        result= max(result,arr[i][0])
        for j in range(1,m):
            if arr[i][j] != 0:
                memo[i][j] = min(memo[i][j-1],memo[i-1][j],memo[i-1][j-1])+1
                result=max(memo[i][j],result)

    return result**2




print(big_rectangle(n,m))

# for _ in memo:
#     print(_)



