# 버블 정렬 알고리즘 구현하기 (개선 3)
# 마지막으로 변경한 위치를 index로 정렬이 완료된 부분 절체

from typing import MutableSequence
import random


#인덱싱식으로 범위제한
def bubble_sort3(a: MutableSequence)-> None:

    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    
    n = len(a)
    k = 0
    
    while k < n-1:
        last = n-1
        for j in range(n-1,k,-1):
            ccnt+=1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j],a[j-1]
                last = j
                scnt+=1

        k= last
    
    print(f'비교 횟수: {ccnt}')
    print(f'교환 횟수: {scnt}')
        

if __name__ == '__main__':
    print('버블정렬을 수행 합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x= [None] * num # 원소수가 num인 배열을 생성
    

    for i in range(num):
        x[i] = random.randrange(1,100)
        
    bubble_sort3(x)
    
    print('오름차순으로 정렬')
    #for i in range(num):
        #print(f'x[{i}] = {x[i]}',end=' ')