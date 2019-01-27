# 给定两个字符串，如果needle在haystack中出现过，返回出现的位置，否则返回-1。
# Input: haystack = "hello", needle = "ll"
# Output: 2

# 思路：
# 借助字符串函数直接实现。

class Solution:
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        return index

if __name__ == '__main__':
    haystack = 'hello'
    needle = 'll'
    s = Solution()
    result = s.strStr(haystack, needle)
    print(result)
