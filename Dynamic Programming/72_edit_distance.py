# 给定两个单词word1和word2，找从word1转换到word2的最小操作次数（操作为：插入、删除、替换）。
# Input: word1 = "horse", s2 = "ros"
# Output: 3 (1:horse -> rorse；2:rorse -> rose; 3: rose -> ros)

# 思路：
# dp[i][j]为word1的前i个字母转化为word2的前j个字母的最小操作次数。
# 如果word[i] == word[j]，则dp[i][j] = dp[i - 1][j - 1]。
# 如果word[i] != word[j], 则dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

class Solution:
    def minDistance(self, word1, word2):
        dp = [[0] * (len(word2) + 1)for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] + 1, dp[i][j] + 1)
        return dp[len(word1)][len(word2)]

if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    s = Solution()
    result = s.minDistance(word1, word2)
    print(result)