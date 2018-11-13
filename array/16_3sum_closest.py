# 给定一个数组和一个target，查找数组中a + b + c 的值最接近target的数字组合，返回该组合的和
# Input: [-1, 2, 1, -4], target = 1
# Output: -1 + 2 + 1 = 2

# 思路1：
# 三重循环暴力求解

# 思路2:
# 先排序，单次循环，两个指针位于前后，同时往中间查找

class Solution:
    def threeSumClosest(self, nums, target):
        result = []
        closest = 1000
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    sub = [nums[i], nums[j], nums[k]]
                    sub.sort()
                    if sub not in result:
                        result.append(sub)
                        diff = abs(target - (nums[i] + nums[j] + nums[k]))
                        if diff < closest:
                            closest = diff
                            sum = nums[i] + nums[j] + nums[k]
                    else:
                        continue
                    k = k + 1
                j = j + 1
        return sum

class solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = 1000
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum)
                if diff < closest:
                    closest = diff
                    result = sum
                if diff == 0:
                    return target
                elif sum < target:
                    left = left + 1
                else:
                    right = right - 1
        return result

if __name__ == '__main__':
    nums = [-1, 2, 1, 4]
    target = 1
    s = Solution()
    result = s.threeSumClosest(nums, target)
    print(result)
    S = solution()
    S_result = S.threeSumClosest(nums, target)
    print(S_result)