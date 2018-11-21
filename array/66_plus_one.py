# 给定一个用数组表示的非负数，对该数加1，该数的最高位位于数组头部（123表示为数组[1, 2, 3]）
# Input: [1,2,3]
# Output: [1,2,4]

# 思路：
# 末位数字 < 9时，直接末位数 + 1
# 末位数字 = 9时，置0前一位 + 1
# 全部为9时，全部置0，首位添加1
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
            return digits

if __name__ == '__main__':
    digits = [1, 2, 3]
    s = Solution()
    result = s.plusOne(digits)
    print(result)