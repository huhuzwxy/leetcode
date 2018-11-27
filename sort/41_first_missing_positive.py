#找到一个未排序数组中未出现的最小整数
#Input: [1, 2, 0]
#Output: 3
#要求：时间复杂度O(n),空间复杂度O(1)

#思路：
#类似桶排序，正确数字放在正确位置上，遍历数组完成
#遍历数组，找到第一个不正确的位置

#问题，如果数组中数值大小全部大于数组长度，怎么办

class Solution:
    def firstMissingPositive(self, nums):
        #直接.sort()时间复杂度不对
        #nums.sort()
        l = len(nums)
        for i in range(l):
            if (nums[i] != i + 1) and (nums[i] < l):
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        print('sort:',nums)
        for i in range(l):
            if nums[i] != i + 1:
                return i + 1

if __name__ == '__main__':
    nums = [1, 2, 0]
    print(nums)
    s = Solution()
    result = s.firstMissingPositive(nums)
    print(result)
