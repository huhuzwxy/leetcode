# 给定字符串S和T，找S中有多少个子串等于T，（S的子串不改变S中元素的相对位置）
# Input: S = "rabbbit", T = "rabbit"
# Output: 3

# 思路：
# dp[i][j]表示字符串S的前i个字符中有多少个子串等于T的前j个字符

class Solution:
    def numDistance(self, s, t):
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        for k in range(len(s) + 1):
            dp[0][k] = 1
        for i in range(len(t)):
             for j in range(len(s)):
                 if s[j] == t[i]:
                     dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                 else:
                     dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[len(t)][len(s)]

if __name__ == '__main__':
    s = 'rabbbit'
    t = 'rabbit'
    S = Solution()
    result = S.numDistance(s, t)
    print(result)
