# 给定一个序列[1, 2, 3, ... , n]，其长度为n（n为1至9），给定一个数k（k为1至n!），输出该序列全排列中的第k个序列
# Input: n = 4, k = 9
# Output: 2314

# 思路：
# 首位数每个数字重复次数为(n - 1)!
# 第二位数每个数字重复次数为(n - 2)!
# ......
# 末位数字每个数字重复次数为1
# 用除法和取余操作上述步骤，放弃减法和乘法！！！

import math

class Solution:
    def getPermutation(self, n, k):
        fact = [1] * n
        nums = [x for x in range(1, n + 1)]
        result = []
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        i = n
        while i > 0:
            j = k / fact[i - 1]
            k = k % fact[i - 1]
            j = math.ceil(j)
            result.append(nums[j - 1])
            nums.pop(j - 1)
            i = i - 1
        return result

if __name__ == '__main__':
    n = 4
    k = 9
    s = Solution()
    result = s.getPermutation(n, k)
    print(result)


