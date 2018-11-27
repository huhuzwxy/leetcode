# 给定一个数组，返回其最大子数组的和
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

# 思路：
# 加完之后小于当前值，则从该值重新开始加，前面的放弃
# 维护一个max_sum记录当前最大值

class Solution:
    def maxSubarray1(self, nums):
        sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            sum = sum + nums[i]
            sum = max(sum, nums[i])
            max_sum = max(sum, max_sum)
        return max_sum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    result = s.maxSubarray1(nums)
    print(result)
