# 给定一个字符串，找其最长回文子串。
# Input: "babad"
# Output: "bab"

# 思路：
# 逆序，动态规划找两个字符串的最长公共子串。
# 或者直接用动态规划。

class Solution:
    def longestPalinrome(self, s):
        j = 0
        s_reverse = [0 for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            s_reverse[j] = s[i]
            j += 1
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        max_len = 0
        p = 0
        for i in range(len(s)):
            for j in range(len(s_reverse)):
                if s[i] == s_reverse[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if dp[i + 1][j + 1] > max_len:
                        max_len = dp[i + 1][j + 1]
                        p = i + 1
                else:
                    dp[i + 1][j + 1] = dp[i - 1][j] if dp[i - 1][j] > dp[i][j - 1] else dp[i][j - 1]
        return s[p - max_len : p]

if __name__ == '__main__':
    s = Solution()
    str = "cbbd"
    result = s.longestPalinrome(str)
    print(result)