# 沿环形路线有n个加油站，每个加油站i有油gas[i]，车从加油站i到i + 1的耗油量为cost[i]，输出从那个点开始车可以顺时针一圈，没有则输返回1。
# Input: gas  = [1,2,3,4,5]
#        cost = [3,4,5,1,2]
# Output: 3

# 思路：
# sum(gas) >= sum(cost)，则一定有解
# 如果A恰好不能到C，则AC中间的点也不能到C

class Solution:
    def canCompleteCircuit(self, gas, cost):
        l = len(gas)
        tank = strat = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(l):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        if tank < 0:
            return - 1
        else:
            return start

if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()
    result = s.canCompleteCircuit(gas, cost)
    print(result)