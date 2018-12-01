# 给定一个2D矩阵，填充0或1，找全部填充1的最大矩形，返回其面积。
# Input: [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

# 思路：
# 计算每列深度，然后同84方法

class Solution:
    def largestRectangle(self, height):
        height.append(0)
        stack = [-1]
        result = 0
        for i in range(len(height)):
            while(height[i] < height[stack[-1]]):
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        return result

    def maximalRectangle(self, matrix):
        max_result = 0
        height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
            result = self.largestRectangle(height)
            max_result = max(max_result, result)
        return max_result

if __name__ == '__main__':
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
    s = Solution()
    result = s.maximalRectangle(matrix)
    print(result)

