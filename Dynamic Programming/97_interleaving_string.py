# 给定字符串s1、s2和s3，判断字符串s3是否能由s1和s2交替组成。
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# 思路：
# dp[i][j]为s3中的前i + j个字符能否由s1中的前i个字符和s2中的前j个字符组成
# s3[i + j] == s1[i]，且dp[i - 1][j] = True，则返回True
# s3[i + j] == s2[j]，且dp[i][j - 1] = True，则返回True

class Solution:
    def isInterLeave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i == j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s3[j - 1] == s2[j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s3[i - 1] == s1[i - 1]
                else:
                    dp[i][j] = (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]) or (s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])
        return dp[len(s1)][len(s2)]

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s = Solution()
    result = s.isInterLeave(s1, s2, s3)
    print(result)

