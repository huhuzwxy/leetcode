import math

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = math.floor((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    s = Solution()
    result = s.search(nums, 5)
    print(result)