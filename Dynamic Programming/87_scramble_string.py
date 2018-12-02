# 给定字符串s1，递归的将其分为两个非空子串，选择某个非叶子结点，交换其左右子数，判断字符串s2是否可由该操作得到。
# Input: s1 = "great", s2 = "rgeat"
# Output: true

# 思路：
# dp[i][j][n]为以i为起点的s1和以j为起点的s2，长度均为n，是否互为scramble。
# 将s1、s2划分为两段，判断左左右右是否是scramble，或者左右左右是否是scramble。

class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        dp = [[[False for i in range(len(s1) + 1)] for j in range(len(s1))] for k in range(len(s1))]
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i][j][1] = s1[i] == s2[j]
        for l in range(2, len(s1) + 1):
            for i in range(len(s1) - l + 1):
                for j in range(len(s2) - l + 1):
                    for k in range(1, l):
                            dp[i][j][l] = (dp[i][j][k] and dp[i + k][j + k][l - k]) or (dp[i][j + l - k][k] and dp[i + k][j][l - k])
        return dp[0][0][len(s1)]

if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    s = Solution()
    result = s.isScramble(s1, s2)
    print(result)

