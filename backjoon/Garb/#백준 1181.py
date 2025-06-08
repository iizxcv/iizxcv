#백준 1181
import sys
sys.stdin = open("input.txt","r")
'''
def str_to_ascii(a):
    result = []
    for c in a:
        result.append(ord(c))
    return result
'''
'''
def str_sort(a):
    
    arr = [item.replace("\n","") for item in set(a)]
    result = [(name, str_to_ascii(name)) for name in arr]
    print(result)
    sorted_result = [sorted(result, key=lambda x:x[1])]
    result = [item[0] for item in sorted_result]
    
    
    
    return result
'''

n = int(input())

a = ['' for _ in range(n)]
#print(a)
for i in range(0, len(a)):
    a[i]= sys.stdin.readline()

# print(str_sort(a))
#print(ord('\n'))
#arr = str_sort(a)
# arr = str_to_ascii(a)
# arr = list(map(str.rstrip,a))
arr1 = [s.strip() for s in set(a)]
arr = sorted(arr1, key=lambda x:(len(x),x))
for _ in arr:
    print(_)


'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''