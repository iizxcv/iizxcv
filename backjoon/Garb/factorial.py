def squre_sum(n, total=1):
    if n==0:
        return total

    return squre_sum((n-1),total*n)


a= int(input())
print(squre_sum(a))

