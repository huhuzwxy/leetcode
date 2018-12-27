# 给定一个整型数组，除了一个元素外每个元素均出现三次，找到仅出现一次的元素
# Input: [2, 2, 3, 2]
# Output: 3

# 思路：
# 二进制实现
# 我选择字典，简单粗暴

class Solution:
    def singleNumber(self, nums):
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for key in dict.keys():
            if dict[key] == 1:
                word = key
        return word

if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    s = Solution()
    result = s.singleNumber(nums)
    print(result)