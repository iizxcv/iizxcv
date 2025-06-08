#버블 정렬 알고리즘

from typing import MutableSequence
import random
from bubble_sort3 import bubble_sort3
import copy

def bubble_sort(a: MutableSequence)-> None:
    """버블 정렬"""
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    
    n = len(a)
    
    
    for i in range(n):
        exchange = 0
        for j in range(n-1,i,-1):
            ccnt+=1
            if a[j -1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]
                exchange+=1
                scnt+=1
        if exchange == 0:
            break
                
    
    print(f'정렬 비교 횟수: {ccnt}')
    print(f'정렬 교환 횟수: {scnt}')



if __name__ == '__main__':
    print('버블정렬을 수행 합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x= [None] * num # 원소수가 num인 배열을 생성
    

    for i in range(num):
        x[i] = random.randrange(1,100)
    
    y = copy.deepcopy(x)
        
    bubble_sort(x)
    bubble_sort3(y)
    
    print('오름차순으로 정렬')
    #for i in range(num):
        #print(f'x[{i}] = {x[i]}',end=' ')
        
    