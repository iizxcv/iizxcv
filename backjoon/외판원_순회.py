import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(sys.stdin.readline())
    W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    INF = float('inf')
    VISITED_ALL = (1 << N) - 1

    # dp[현재도시][방문상태] = 최소비용
    dp = [[-1] * (1 << N) for _ in range(N)]

    def dfs(cur, visited):
        if visited == VISITED_ALL:
            return W[cur][0] if W[cur][0] != 0 else INF
        if dp[cur][visited] != -1:
            return dp[cur][visited]
        min_cost = INF
        for next_city in range(N):
            if not (visited & (1 << next_city)) and W[cur][next_city] != 0:
                cost = dfs(next_city, visited | (1 << next_city)) + W[cur][next_city]
                if cost < min_cost:
                    min_cost = cost
        dp[cur][visited] = min_cost
        return min_cost

    answer = dfs(0, 1 << 0)
    print(answer)

if __name__ == "__main__":
    main()
