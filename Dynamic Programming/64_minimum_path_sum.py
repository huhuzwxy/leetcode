# 给定一个大小为mxn的矩阵，元素为非负数，找到从左上角到右下角的最短路径。
# Input: [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7（1 + 3 +1 + 1）

# 思路：
# dp[i][j]为矩阵元素gird(i, j)处的最短路径
# 状态转移方程：dp[m][n] = min(dp[m][n - 1], dp[m - 1][n]) + grid[m][n]。

class Solution:
    def minPathSum(self, grid):
        dp = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        for i in range(len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for j in range(len(grid[0])):
            dp[j][0] = grid[j][0] + dp[j - 1][0]
        for m in range(1, len(grid)):
            for n in range(1, len(grid[0])):
                dp[m][n] = min(dp[m][n - 1], dp[m - 1][n]) + grid[m][n]
        return dp[len(grid) - 1][len(grid[0]) - 1]

if __name__ == '__main__':
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    s = Solution()
    result = s.minPathSum(grid)
    print(result)