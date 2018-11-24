# 给定一个矩阵m x n，矩阵中某个元素为0，则将该元素对应的行列中剩余元素置0。
# Input: [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

# 思路(有问题，未解决)：
# 查找矩阵，找到某个元素为0，把该行该列置为0。设置一字典，每个元素均置为False，将置为0的全部标记为True，为False时则下一轮置0。
# 注意在置0的行列里还含有0

# 思路1：
# 第一次遍历，记录有0的行号和列号，第二次遍历，将其置0
# 空间复杂度O(m + n)

# 思路2：
# 用第一行第一列来记录该行列是否需要置0（从第2列开始循环）
# 单独设置一个变量用来记录第一列是否有0
# 判断第一行第一个元素是否为0，来确定第一行是否需要置0（第一行其它位置有0，则第一个元素已置0；若其它位置无0，则只需判读第一个是否是0）
# 空间复杂度O(1)

import numpy as np

class Solution:
    def setZeroes(self, matrix):
        dict = {}
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                dict[str(i) + str(j)] = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and dict[str(i) + str(j)] == False:
                    for sj in range(n):
                        matrix[i][sj] = 0
                        dict[str(i) + str(sj)] = True
                    for si in range(m):
                        matrix[si][j] = 0
                        dict[str(si) + str(j)] = True
        return matrix

    def setZeroes1(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
        return matrix

    def setZeroes2(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        first_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if first_col == True:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

if __name__ == '__main__':
    matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    s = Solution()
    #result = s.setZeroes(matrix)
    #print(result)
    #result1 = s.setZeroes1(matrix)
    #print(result1)
    result2 = s.setZeroes2(matrix)
    print(result2)

