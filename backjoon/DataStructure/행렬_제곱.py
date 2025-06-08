import sys


def mat_power(arr1,arr2):
    size = len(arr1)
    answer = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for k in range(size):
            for j in range(size):
                answer[i][k] += (arr1[i][j] * arr2[j][k]) % 1000
    return answer
     
     
def multi(arr,n):
    
    if n == 1:
        return arr
    temp = mat_power(arr,arr)
    if n % 2 == 0:
        return mat_power(temp,temp)
    else:
        return mat_power(mat_power(temp,temp),arr)    




n,p = map(int,input().split(' '))

a=[[]]
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    a.append(row)

a= a[1:]

result= multi(a,p)

for i in range(n):
    for j in range(n):
        result[i][j] = result[i][j] % 1000 
        print(result[i][j], end=" ")
    print()


print()
#print(a)

