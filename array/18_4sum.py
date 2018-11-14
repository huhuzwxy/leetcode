# 给定一个数组和一个target，查找数组中a + b + c + d = target的数字组合，返回该组合
# Input: [1, 0, -1, 0, -2, 2], target = 0
# Output: [
#           [-1, 0, 0, 1],
#           [-2, -1, 1, 2],
#           [-2, 0, 0, 2]
#          ]

# 思路1：
# 3sum三重循环 + 哈希表

# 思路2：
# 同3sum（两重循环 + 左右两个指针）

# 思路3：
# 利用哈希表，两个数之和存入哈希表，双重循环查找哈希表即可

class Solution:
    def foursum(self, nums, target):
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    dict = {x: False for x in nums}
                    temp = target - nums[i] - nums[j] - nums[k]
                    if temp in dict:
                        dict[nums[i]] = True
                        dict[nums[j]] = True
                        dict[nums[k]] = True
                        sub_result = [nums[i], nums[j], nums[k], temp]
                        sub_result.sort()
                        if sub_result not in result and dict[temp] == False:
                            result.append(sub_result)
                            dict[temp] = True
                    #print('dict = ', dict)
                    k = k + 1
                j = j + 1
        return result

class solution:
    def foursum(self, nums, target):
        nums.sort()
        dict = {}
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = nums[i] + nums[j]
                if val not in dict:
                    dict[val] = [[i, j]]
                else:
                    dict[val].append([i, j])

        for m in range(len(nums)):
            for n in range(m + 1, len(nums)):
                find_val = target - nums[m] - nums[n]
                if find_val in dict:
                    for k in dict[find_val]:
                        sub_result = [nums[m], nums[n], nums[k[0]], nums[k[1]]]
                        sub_result.sort()
                        if k[0] > n and sub_result not in result:
                            result.append(sub_result)
        return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    s = Solution()
    result = s.foursum(nums, target)
    print(result)
    S = solution()
    result1 = S.foursum(nums, target)
    print(result1)