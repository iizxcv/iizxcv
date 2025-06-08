from itertools import product

lst = [1, 3, 5]
target = 10
result = []
product_cnt = 0

# 최대 길이는 target // min(lst) → 모든 1로 채웠을 때 길이
for r in range(1, target + 1):
    for comb in product(lst, repeat=r):
        product_cnt +=1
        
        if sum(comb) == target:
            result.append(comb)

# 출력
for seq in result:
    print(seq)
print(len(result))
print(product_cnt)
