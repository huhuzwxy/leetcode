# 给定一个数组和一个value，删除数组中所有的value，返回现在数组的长度，空间复杂度O(1)
# Input: [3, 2, 2, 3], target = 3
# Output: 2

# 思路1：
# 顺序查找，前后两个指针，等于value的交换到最后面

# 思路2：
# 顺序查找，前后两个指针，不用理会等于value的值，碰到直接把后指针的赋值过来

class Solution:
    def removeElement(self, nums, val):
        l = len(nums)
        j = l - 1
        for i in range(l):
            if nums[i] == val and j > i:
                l = l - 1
                while nums[j] == val:
                    j = j - 1
                    l = l - 1
                nums[i], nums[j] = nums[j], nums[i]
                j = j - 1
            else:
                continue
        return l

class solution:
    def removeElement(self, nums, val):
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == val:
                nums[i] = nums[l - 1]
                l = l - 1
            else:
                i = i + 1
        return l

if __name__ == '__main__':
    #nums = [0, 1, 2, 2, 3, 0, 4, 2]
    #target = 2
    nums = [3, 2, 2, 3]
    target = 3
    s = Solution()
    result = s.removeElement(nums, target)
    print(result)
    S = solution()
    result1 = S.removeElement(nums, target)
    print(result1)
