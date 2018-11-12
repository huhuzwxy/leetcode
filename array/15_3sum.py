# 给定一个数组，查找数组中a + b + c = 0的数字组合，返回该组合
# Input: [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 0, 1], [-1, -1, 2]]

# 思路：
# 哈希表

class Solution:
    def threeSum(self, nums):
        result = []
        dict = {x: False for x in nums}
        for i in range(len(nums) - 1):
            dict[nums[i]] = True
            current = i + 1
            while dict[nums[i]] == True and current < len(nums):
                print('current = ', current)
                print(nums[i], nums[current], -(nums[i] + nums[current]))
                sub = [nums[i], nums[current], -(nums[i] + nums[current])]
                sub.sort()
                if -(nums[i] + nums[current]) in dict and dict[-(nums[i] + nums[current])] == False:
                    if sub not in result:
                        result.append(sub)
                    current = current + 1
                else:
                    current = current + 1
                print('sub = ', dict)
                print('result = ', sub)
            print(dict)
        return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    result = s.threeSum(nums)
    print(result)