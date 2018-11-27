# 给定一个已排序数组，去掉重复元素，返回数组长度。空间复杂度O(1)
# Input: [1, 1, 2]
# Output: length = 2

# 思路：
# 设置两个指针，一个用来存储不同的，一个遍历数组。

class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        j = 1
        for i in range(l - 1):
            if nums[i + 1] == nums[i]:
                continue
            else:
                nums[j] = nums[i + 1]
                j = j + 1
        k = l - 1
        while k >= j:
            del nums[k]
            k = k - 1
        print('nums:', nums)
        return j

if __name__ == '__main__':
    nums = [0, 0 ,1, 1, 1, 2, 2, 3, 3, 4]
    nums.sort()
    print('nums:', nums)
    s = Solution()
    result = s.removeDuplicates(nums)
    print('length = ', result)