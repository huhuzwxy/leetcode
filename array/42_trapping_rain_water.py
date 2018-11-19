# 给定一个非负整数序列，其数值k表示k个高度为1的小块，计算能有多少个闭合框
# Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6

class Solution:
    def trap(self, height):
        num = 0
        i = 0
        start_val = end_val = 0
        while i < len(height) - 2:
            if height[i + 1] > height[i]:
                i = i + 1
            else:
                start = i
                start_val = height[start]
                i = i + 1
                if height[i + 1] < height[i]:
                    i = i + 1
                else:
                    mid = i
                    mid_val = height[mid]
                    i = i + 1
                    if height[i + 1] > height[i]:
                        i = i + 1
                    else:
                        end = i
                        end_val = height[end]
                        i = i + 1
                if start_val and end_val:
                    if start_val < end_val:
                        num = num + pow(mid - start, 2)
                    else:
                        num = num + pow(end - mid, 2)
        return num

if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    result = s.trap(height)
    print(result)
