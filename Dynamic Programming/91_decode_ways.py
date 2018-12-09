# A-Z被编码为1-26，给定一个仅包含数字的非空字符串，输出可能的解码数。
# Input: "12"
# Output: 2 ('1 2': A B; '12': L)

# 思路：
# 找有多少个子串，大于等于1，小于等于26
# dp[i]表示从开始至字符串的第i位有多少种解码数
# 判断i - 1位和i位组成的数字是否小于26，注意'0'的判断

class Solution:
    def numDecodings(self, s):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] == '0':
            return False
        else:
            dp[1] = 1
        for i in range(1, len(s)):
            if s[i] <= '6' and s[i - 1] <= '2':
                if s[i] != '0' and s[i - 1] != '0':
                    dp[i + 1] = dp[i] + dp [i - 1]
                elif s[i] == '0' or s[i - 1] == '0':
                    dp[i + 1] = dp[i - 1]
                else:
                    return False
            else:
                if s[i] == '0':
                    return False
                elif s[i - 1] == '0':
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[len(s)]

if __name__ == '__main__':
    s = '12'
    S = Solution()
    result = S.numDecodings(s)
    print(result)

