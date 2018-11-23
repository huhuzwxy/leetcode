# 给定n，打印其格雷码，相邻两个格雷码只有一位不同。
# Input: 2
# Output: [0, 1, 3, 2]
# 对应格雷码：00, 01, 11, 10

# 思路：
# n = 3时，为000, 001, 011, 010, 110, 111, 101, 100从中点为中心，后两位是对称的，即由前一半可得到整个序列
# 表示成序列为[0, 1, 1 + 2^1, 0 + 2^1]

class Solution:
    def grayCode(self, n):
        if n == 0:
            return[0]
        if n == 1:
            return [0, 1]
        res = self.grayCode(n - 1)
        sub_res = pow(2, n - 1)
        for i in range(sub_res - 1, -1, -1):
            res.append(res[i] + sub_res)
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.grayCode(3)
    print(result)







