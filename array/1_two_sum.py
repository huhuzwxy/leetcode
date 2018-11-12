# 给定一个数组和一个target，查找数组中相加等于target的两个数，返回其位置
# Input: [2, 7, 11, 15], target = 9
# Output: [0, 1]

# 思路：
# 哈希表/ 暴力求解

class Solution:
    def twosum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
            y = target - nums[i]
            if y in dict:
                return dict[y], i
            print(dict)

class solution:
    def FindAll(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                else:
                    continue


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 26
    s = Solution()
    result = s.twosum(nums, target)
    print(result)
    t = solution()
    result2 = t.FindAll(nums, 9)
    print(result2)
