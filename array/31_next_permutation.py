# 给定一个序列，输出其下一个更大序列，若已最大，则从头开始。时间复杂度O(1)
# 1, 2, 3 -> 1, 3, 2

# 思路：
# 找递增结束的位置，换上比该数大的最小数

class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 1
        if nums[i - 1] >= nums[i]:
            i = i - 1
            print(i)
            if i == 1:
                m = 0
                n = len(nums) - 1
                print(m, n)
                while m <= n:
                    nums[m], nums[n] = nums[n], nums[m]
                    m = m + 1
                    n = n - 1
                    print(m, n)
        else:
            k = 0
            for j in range(i, len(nums)):
                min = nums[j]
                print(j)
                if nums[j] > nums[i - 1] and nums[j] <= min:
                    min = nums[j]
                    k = j
            nums[i - 1], nums[k] = nums[k], nums[i - 1]
        return nums


if __name__ == '__main__':
    nums = [1, 1, 5]
    s = Solution()
    result = s.nextPermutation(nums)
    print(result)



