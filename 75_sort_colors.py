#数组中含红白蓝三颜色，将其按红、白、蓝排序，红色为0，白色为1，蓝色为2
#Input: [2, 0, 2, 1, 1, 0]
#Output: [0, 0, 1, 1, 2, 2]

#思路1：
#第一次遍历数组，分别统计0，1，2的个数
#第二次遍历数组，将0，1，2按个数放入数组中

#思路2：
#只遍历一次数组实现排序
#设置三个指针，一个指向头j，一个指向尾k，一个遍历i
#如果nums[i]==0，将nums[i]与nums[j]交换，i = i + 1, j = j + 1
#如果nums[i]==2，将nums[i]与nums[k]交换，i = i + 1, k = k + 1
#遍历时始终保持i < k，否则尾部已排好序的会被重排

class Solution:
    def sortColors(self, nums):
        l = len(nums)
        m = n = k = 0
        for i in range(l):
            if nums[i] == 0:
                m = m + 1
            elif nums[i] == 1:
                n = n + 1
            elif nums[i] == 2:
                k = k + 1
        for i in range(m):
            nums[i] = 0
        for i in range(m, m + n):
            nums[i] = 1
        for i in range(m + n, m + n + k):
            nums[i] = 2
        return nums

class solution_other:
    def sortColors(self, nums):
        l = len(nums)
        i = j = 0
        k = l - 1
        while i < k:
            if nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j = j + 1
            elif nums[i] == 2:
                nums[k], nums[i] = nums[i], nums[k]
                k = k - 1
            i = i + 1
        return nums

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 1]
    s = Solution()
    result = s.sortColors(nums)
    print(result)
    s1 = solution_other()
    result1 = s1.sortColors(nums)
    print(result1)


