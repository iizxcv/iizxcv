n, m = map(int, input().split())
tree = list(map(int, input().split()))

def cut_tree(trees, cut):
    return sum((t - cut) for t in trees if t > cut)

# 이진 탐색 범위
low = 0
high = max(tree)
answer = 0

while low <= high:
    mid = (low + high) // 2
    total = cut_tree(tree, mid)
    #print(total)
    if total >= m:
        answer = mid  # 조건 만족 → 높이 더 높여볼 수 있음
        low = mid + 1
    else:
        high = mid - 1

print(answer)