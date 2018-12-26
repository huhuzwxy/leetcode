# 给定一个整型数组，除了一个元素外每个元素均出现两次，找到仅出现一次的元素
# Input: [4, 1, 2, 1, 2]
# Output: 4

# 思路：
# 字典存每个数字出现的次数，返回次数为1的数字

# 其它思路：
# 时间复杂度o(n)，空间复杂度o(1)，放弃字典
# 异或操作 a ^ a = 0, a ^ b ^ a = b, a ^ 0 = a

class Solution:
    def SingleNumber(self, nums):
        dict = {}
        index = list(set(nums))
        dict = {index[i]: 0 for i in range(len(index))}
        for i in nums:
            if i in index:
                dict[i] += 1
        return list(dict.keys())[list(dict.values()).index(1)]

    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i
        return result


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    #nums = [2, 2, 1]
    s = Solution()
    result = s.singleNumber(nums)
    print(result)