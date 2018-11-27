#问题：
#合并两个排序数组nums1和nums2至nums1
#Input:
#nums1 = [1, 2, 3, 0, 0, 0], m = 3
#nums2 = [2, 5, 6], n = 3
#Output:nums1 = [1, 2, 2, 3, 5, 6]
#假设nums1有足够大的空间

#我的思路：
#num2[i] <= num1[j]时, num1[j]及其之后的后移，num1[j] = num2[i], 置num_add，每添加一个num_add + 1
#num2[i] > num1[j]时, j++, 继续扫描， 至num1中数字扫描完时， num1[j] = num2[i]

#其它思路：
#从两个列表的最大元素开始比较
#三个指针向前移动
#nums2中的前几个元素为最小元素时，此时j >= 0
#不需要元素移动，空间复杂度O(1)

#我的方法
class Solution:
    def merge(self, nums1, m, nums2, n):
        #nums1.sort()
        #nums2.sort()
        tem_list = [0] * n
        nums1.extend(tem_list)
        num_add = 0
        i = j = 0
        while(i < n):
            #print('i = {}, j = {}'.format(i, j))
            if nums2[i] <= nums1[j]:
                k = m + num_add - 1
                #print('k =', k)
                while(k >= j):
                    #print('k = ', k)
                    nums1[k + 1] = nums1[k]
                    k = k - 1
                nums1[j] = nums2[i]
                num_add = num_add + 1
                i = i + 1
                j = j + 1
            else:
                if nums1[j] == 0:
                    nums1[j] = nums2[i]
                    num_add = num_add + 1
                    i = i + 1
                    j = j + 1
                else:
                    j = j + 1
            #print('sub_sum:', nums1)
        return nums1

#其它方法
class solution_other():
    def merge(self, nums1, m, nums2, n):
        tem_list = [0] * n
        nums1.extend(tem_list)
        i = m - 1
        j = n - 1
        k = m + n - 1
        while(i >= 0 and j >= 0):
            if(nums2[j] >= nums1[i]):
                nums1[k] = nums2[j]
                j = j - 1
                k = k - 1
                #print('sub_nums1:', nums1)
            else:
                nums1[k] = nums1[i]
                i = i - 1
                k = k - 1
                #print('sub_nums1:', nums1)
        while(j >= 0):
            nums1[k] = nums2[j]
            j = j - 1
            k = k - 1
        return nums1

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 7]
    m = len(nums1)
    nums2 = [2, 5, 6, 8]
    n = len(nums2)
    result = s.merge(nums1, m, nums2, n)
    print('result:', result)

    s1 = solution_other()
    nums1 = [1, 2, 7]
    m = len(nums1)
    nums2 = [2, 5, 6, 8]
    n = len(nums2)
    result1 = s1.merge(nums1, m, nums2, n)
    print('result_other:', result1)




