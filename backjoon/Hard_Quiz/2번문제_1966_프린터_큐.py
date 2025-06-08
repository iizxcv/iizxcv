from collections import deque

def printer_queue(n, m, priorities):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        cur = queue.popleft()
        # 현재 문서보다 높은 우선순위가 있는지 확인
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == m:
                return count

# 입력 처리
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(printer_queue(n, m, priorities))
