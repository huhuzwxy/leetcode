# 给定一个未排序数组，找最长连续序列，返回其长度，时间复杂度O(n)
# Input: [100, 2, 40, 4, 5, 3, 1]
# Output: 5

# 思路：
# 哈希表
# 依次查找数组中的每个数是否有左右邻

class Solution:
    def longestConsecutive(self, nums):
        dict = {x: False for x in nums}
        print(dict)
        maxLen = -1
        for i in dict:
            print('i = ', i)
            if dict[i] == False:
                current = i + 1
                lenright = 0
                while current in dict:
                    lenright = lenright + 1
                    dict[current] = True
                    current = current + 1
                current = i - 1
                lenleft = 0
                while current in dict:
                    lenright = lenright + 1
                    dict[current] = True
                    current = current - 1
                maxLen = max(maxLen, lenleft + 1 + lenright)
                print(dict)
        return maxLen

if __name__ == "__main__":
    num = [100, 2, 40, 4, 5, 3, 1]
    s = Solution()
    result = s.longestConsecutive(num)
    print(result)




