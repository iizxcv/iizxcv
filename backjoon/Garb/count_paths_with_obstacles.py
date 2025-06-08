def count_paths_with_obstacles(n, m, obstacles):
    dp = [[0] * m for _ in range(n)]

    # 장애물이 아니면 시작 지점은 1
    if (0, 0) not in obstacles:
        dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if (i, j) in obstacles:
                dp[i][j] = 0  # 장애물이면 경로 없음
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[n - 1][m - 1]

# 격자 크기
n, m = 3, 3

# 장애물 좌표들 (예: (1,1)은 못 감)
obstacles = {(1, 1)}

print("AI가 도달 가능한 경로 수 (장애물 있음):", count_paths_with_obstacles(n, m, obstacles))
