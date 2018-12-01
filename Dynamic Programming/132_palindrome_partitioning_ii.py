# 给定一个字符串，将其切割使得每个子串均为回文串，返回最小切割次数。回文串：逆序后仍为该串。
# Input: 'aab'
# Output: 1（'aa'，'b'）

# 思路：
# dp[i,j] = min{dp[i,k] + dp[k+1,j]}为区间[i,j]的最小切割次数
# 改为一维数组，dp[i] = min{1 + dp[j+1]}
# p[i][j]判断从字符i到字符j是否是回文串
# dp[i]为从字符i到最后的最少切割次数

import numpy as np

class Solution:
    def minCut(self, s):
        dp = [0] * (len(s) + 1)
        for i in range(len(s) + 1):
            dp[i] = len(s) - 1 - i
        print(dp)
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                sub_s = s[i:j + 1]
                #如果s[i:j + 1]不是回文串，切割次数为dp[i]
                #如果s[i:j + 1]是回文串，切割dp[i] = min(dp[i], 1 + dp[j + 1])
                if self.reverse_same(sub_s) == True:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
        return dp[0]

    def reverse_same(self, s):
        if len(s) == 0:
            return False
        l = np.floor(len(s) / 2)
        j = 0
        i = len(s) - 1
        while i >= l:
            if s[j] == s[i]:
                j = j + 1
                i = i - 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = 'aab'
    S = Solution()
    result = S.minCut(s)
    print(result)

