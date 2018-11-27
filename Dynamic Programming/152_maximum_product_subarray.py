# 给定一个数组，返回其最大子数组的乘积
# Input: [-2,0,-1]
# Output: 0

# 思路：
# 有可能负负得正，维护一个最大值、最小值、全局最大值

import numpy as np

class Solution:
    def maxProduct(self, nums):
        product = nums[0]
        maxnums = minnums = nums[0]
        for i in range(1, len(nums)):
            a = maxnums * nums[i]
            b = minnums * nums[i]
            maxnums = max(a, b, nums[i])
            minnums = min(a, b, nums[i])
            product = max(maxnums, product)
        return product

if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    s = Solution()
    result = s.maxProduct(nums)
    print(result)

