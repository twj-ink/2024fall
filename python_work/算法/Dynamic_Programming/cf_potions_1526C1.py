n = int(input())
a = list(map(int, input().split()))

# 定义dp数组
dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0  # 初始化

# 动态规划
for i in range(1, n + 1):  # 遍历每个药水
    for j in range(i + 1):  # 遍历喝药水的数量
        # 如果不喝第 i 个药水
        dp[i][j] = dp[i-1][j]
        # 如果喝第 i 个药水，并且之前的健康值非负
        if j > 0 and dp[i-1][j-1] + a[i-1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1])

# 找到最大喝药水的数量
result = 0
for j in range(n + 1):
    if dp[n][j] >= 0:
        result = j

print(result)
