# 给定一个n x n矩阵，将其顺时针旋转90度，空间复杂度O（1）
# Input: [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# Output: [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# 思路：
# 旋转后i行j列会变为j列(n - i - 1)列

import math

class Solution:
    def rotate(self, matrix):
        l = len(matrix)
        for i in range(math.floor(l / 2)):
            for j in range(math.ceil(l / 2)):
                print('i, j = ', i, j)
                temp = matrix[j][l - i - 1]
                matrix[j][l - i - 1] = matrix[i][j]
                matrix[i][j] = matrix[l - j - 1][i]
                matrix[l - j - 1][i] = matrix[l - i - 1][l - j - 1]
                matrix[l - i - 1][l - j - 1] = temp
                print('matrix = ', matrix)
        return matrix

if __name__ == '__main__':
    matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
    s = Solution()
    result = s.rotate(matrix)
    print(result)