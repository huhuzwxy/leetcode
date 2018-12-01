# 给定一个数组，第i个元素为第i天股票的价格，求最高利润，只能交易两次。
# Input: [3,3,5,0,0,3,1,4]
# Output: 6（第4天买，第6天卖，3-0=3；第七天买，第八天卖，4-1=3）

# 思路：
# 前i天求一次最大利润，后i天求一次最大利润
# pre_max_profit[i]为前i天的最大利润
# pro_max_profit[i]为后i天的最大利润

class Solution:
    def maxProfit(self, prices):
        pre_max_profit = [0] * len(prices)
        pro_max_profit = [0] * len(prices)
        pre_min_buy = prices[0]
        for i in range(1, len(prices)):
            pre_min_buy = min(pre_min_buy, prices[i])
            pre_max_profit[i] = max(pre_max_profit[i - 1], prices[i] - pre_min_buy)
        print(pre_max_profit)
        pro_max_sell = prices[len(prices) - 1]
        for j in range(len(prices) - 2, -1, -1):
            pro_max_sell = max(pro_max_sell, prices[j])
            pro_max_profit[j] = max(pro_max_profit[j + 1], pro_max_sell - prices[j])
        print(pro_max_profit)
        max_profit = 0
        for k in range(len(prices)):
            max_profit = max(max_profit, pre_max_profit[k] + pro_max_profit[k])
        return max_profit

if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    s = Solution()
    result = s.maxProfit(prices)
    print(result)

