# 给定一个字符串，判断其是否是回文数。只考虑字母数字字符，不考虑大小写。
# Input: "A man, a plan, a canal: Panama"
# Output: True

# 思路：
# 借助list函数实现。
# s.lower()将大写转化为小写
# s.isalnum()是字母或者数字；s.isalpha()是字母；s.isdigit()是数字
# s.reverse()字符串逆序

class Solution:
    def isPalindrome(self, s):
        a = new_list = [c for c in s.lower() if c.isalnum()]
        new_list.reverse()
        return a == new_list

if __name__ == '__main__':
    str = "A man, a plan, a canal: Panama"
    s = Solution()
    result = s.isPalindrome(str)
    print(result)
