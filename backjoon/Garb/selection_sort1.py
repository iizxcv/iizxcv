# 단순 선택 정렬 알고리즘 구현

from typing import MutableSequence

"""단순 선택 정렬"""
def selection_sort(a: MutableSequence) -> None:
        
    n = len(a)
    for i in range(n-1):
        min = i # 정렬할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i] #정렬할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환
        
        print(a)

        
        
if __name__ == '__main__':
    
    n = int(input('배열 개수 입력해주세요'))
    
    a = [None]*n
    
    for i in range(n):
        a[i] = int(input('원소 입력'))
    
    selection_sort(a)