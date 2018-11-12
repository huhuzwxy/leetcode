# 给定两个已排序数组，找中位数，时间复杂度O(log(m+n))
# Input: [1, 2], [3, 4]
# Output: 2.5

# 思路：
# 找第k小

import math

class Solution:
    def FindMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 1:
            return self.FindKth(nums1, nums2, math.floor(m + n) / 2 + 1)
        else:
            return (self.FindKth(nums1, nums2, (m + n) / 2) + self.FindKth(nums1, nums2, (m + n) / 2) + 1) / 2

    def FindKth(self, nums1, nums2, k):
        #找两个数组的第k小
        m = len(nums1)
        n = len(nums2)
        if n > m:
            return self.FindKth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        k1 = int(min(k // 2, m))
        k2 = int(k - k1)
        if nums1[k1 - 1] <= nums2[k1 - 1]:
            return self.FindKth(nums1[k1: ], nums2, k2)
        else:
            return self.FindKth(nums1, nums2[k1: ], k2)

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    result = s.FindMedianSortedArrays(nums1, nums2)
    print('median = ', result)


