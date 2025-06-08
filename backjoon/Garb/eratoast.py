import math
import sys

def sieve(limit: int) -> list[int]:
    is_prime = [True]*(limit+1)
    is_prime[0:2] = [False, False]

    for p in range(2, int(math.sqrt(limit))+1):
        if is_prime[p]:
            for multiple in range(p*p, limit+1, p):
                is_prime[multiple] = False
    return [x for x, prime in enumerate(is_prime) if prime]

def goldbach(n: int) -> tuple[int, int] | None:
    
    if n < 4 or n % 2:
        raise ValueError("골드바흐 검증은 4이상의 짝수에서만 의미 있음")
    
    lst = sieve(n)
    lst_set = set(lst)
    #print(lst)
    for p in lst[(len(lst)//2):len(lst):]:
        q = n - p  ## 소수리스트를 순회하며 n - p를 q에 연결
        if q in lst_set: #집합안에 포함되어 있는지 비교
            return q,p
    

# 테스트
no = int(input())
even= [0 for _ in range(no)]
for _ in range(no):
    even[_] = int(sys.stdin.readline())

for _ in even:  
    p, q = goldbach(_)
    print(f"{p} {q}")