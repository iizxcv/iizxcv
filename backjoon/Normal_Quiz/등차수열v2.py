def list_num(n:int)->list:
    result = []
    while n > 0:
        result.append(n%10)
        n//=10
    return result[::-1]

a = 10
print(list_num(a))