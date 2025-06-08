def  subtraction(x):
    result = x[0]
    for i in range(1,len(x)):
        result -= int(x[i])
    #print(result)
    return result

n = input().split('-')
#print(n)
c=[]

for a in n:
    b = list(map(int,a.split('+')))
    c.append(sum(b))
    #print(b)


print(subtraction(c))