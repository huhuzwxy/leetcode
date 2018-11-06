# 给定一个已排序数组，同一个重复元素最多允许出现两次，返回数组长度。空间复杂度O(1)
# Input: [1, 1, 1, 2, 2, 3]
# Output: length = 5

# 思路：
# 设置三个指针i, j, k
# i用来遍历数组
# k用来判断元素的重复次数，重复一次时j = j + 1，其它重复次数j不移动，在出现不重复时将k置0
# j用来存放应得数组

class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        j = 1
        k = 0
        for i in range(l - 1):
            if nums[i] == nums[i + 1]:
                k = k + 1
                if k == 1:
                    j = j + 1
            else:
                nums[j] = nums[i + 1]
                j = j + 1
                k = 0
        m = l - 1
        while m >= j:
            del nums[m]
            m = m - 1
        print('nums:', nums)
        return j

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums.sort()
    print('nums:', nums)
    s = Solution()
    result = s.removeDuplicates(nums)
    print('length = ', result)


