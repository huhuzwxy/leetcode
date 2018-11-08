import math

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = math.floor((left + right) / 2)
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                if nums[mid] > nums[left] or nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= nums[left] or nums[left] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    s = Solution()
    result = s.search(nums, 3)
    print(result)
