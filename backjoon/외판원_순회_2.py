import sys
import math
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
INF = math.inf
VISITED_ALL = (1 << n) - 1

dp = [[-1] * (1 << n) for _ in range(n)]

def travel(current, visited):
    if visited == VISITED_ALL:
        return edges[current][0] if edges[current][0] != 0 else INF
    if dp[current][visited] != -1:
        return dp[current][visited]
    ans = INF
    for next_city in range(n):
        if not (visited & (1 << next_city)) and edges[current][next_city] != 0:
            cost = travel(next_city, visited | (1 << next_city)) + edges[current][next_city]
            if cost < ans:
                ans = cost
    dp[current][visited] = ans
    return ans

print(travel(0, 1 << 0))
