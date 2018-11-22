# 爬台阶，n步可爬到顶端，每次可爬1步或2步，有多少种方式爬到顶端
# Input: 3
# Output: 3 [(1, 1, 1), (1, 2), (2, 1)]

# 思路：
# 假设第一次爬1步，则还有n - 1级台阶；假设第一次爬2步，则还有n - 2级台阶
# 递归表示为f(n) = f(n - 1) + f(n - 2)
# 即为斐波那契数列求解
# 1.直接递归（n较大时，耗时）
# 2.存储每次计算的结果，下次直接用
# 3.[[1, 1], [1, 0]]的幂乘算法
# 4.通项公式

class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        while n > 2:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        for i in range(2, n):
            third = first + second
            first = second
            second = third
        return second

if __name__ == '__main__':
    s = Solution()
    result = s.climbStairs(4)
    print(result)
    result1 = s.climbStairs1(4)
    print(result1)
